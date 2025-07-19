# Copyright 2025 Jiaqi Liu. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import logging
import re
from typing import Callable

import yaml

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

"""
The language identifier for German language.

.. py:data:: GERMAN
   :value: German
   :type: string
"""
GERMAN = "German"

"""
The language identifier for German language.
.. py:data:: ITALIAN
   :value: Italian
   :type: string
"""
ITALIAN = "Italian"

"""
The language identifier for Latin language.

.. py:data:: LATIN
   :value: Latin
   :type: string
"""
LATIN = "Latin"

"""
The language identifier for Ancient Greek.

.. py:data:: ANCIENT_GREEK
   :value: Ancient Greek
   :type: string
"""
ANCIENT_GREEK = "Ancient Greek"

EXCLUDED_INFLECTION_ENTRIES = [
    "",
    "singular",
    "plural",
    "masculine",
    "feminine",
    "neuter",
    "nominative",
    "genitive",
    "dative",
    "accusative",
    "N/A"
]

ENGLISH_PROPOSITIONS = {
    "about", "above", "across", "after", "against", "along", "among", "around", "at", "before", "behind", "below",
    "beneath", "beside", "between", "beyond", "by", "down", "during", "except", "for", "from", "in", "inside", "into",
    "like", "near", "of", "off", "on", "onto", "out", "outside", "over", "past", "since", "through", "throughout", "to",
    "toward", "under", "underneath", "until", "up", "upon", "with", "within", "without"
}
EXCLUDED_DEFINITION_TOKENS = {"the"} | ENGLISH_PROPOSITIONS


def get_vocabulary(yaml_path: str) -> list:
    with open(yaml_path, "r", encoding='utf-8') as f:
        return yaml.safe_load(f)["vocabulary"]


def get_definitions(word) -> list[(str, str)]:
    """
    Extract definitions from a word as a list of bi-tuples, with the first element being the predicate and the second
    being the definition.

    For example (in YAML)::

    definition:
      - term: nämlich
        definition:
          - (adj.) same
          - (adv.) namely
          - because

    The method will return `[("adj.", "same"), ("adv.", "namely"), (None, "because")]`

    The method works for the single-definition case, i.e.::

    definition:
      - term: na klar
        definition: of course

    returns a list of one tupple `[(None, "of course")]`

    Note that any definition are converted to string. If the word does not contain a field named exactly "definition", a
    ValueError is raised.

    :param word:  A dictionary that contains a "definition" key whose value is either a single-value or a list of
                  single-values
    :return: a list of two-element tuples, where the first element being the predicate (can be `None`) and the second
             being the definition
    """
    logging.info("Extracting definitions from {}".format(word))

    if "definition" not in word:
        raise ValueError("{} does not contain 'definition' field. Maybe there is a typo".format(word))

    predicate_with_definition = []

    definitions = [word["definition"]] if not isinstance(word["definition"], list) else word["definition"]

    for definition in definitions:
        definition = str(definition)

        definition = definition.strip()

        match = re.match(r"\((.*?)\)", definition)
        if match:
            predicate_with_definition.append((match.group(1), re.sub(r'\(.*?\)', '', definition).strip()))
        else:
            predicate_with_definition.append((None, definition))

    return predicate_with_definition


def get_attributes(
        word: object,
        language: str,
        node_label_attribute_key: str,
        inflection_supplier: Callable[[object], dict] = lambda word: {}
) -> dict[str, str]:
    """
    Returns a flat map as the Term node properties stored in Neo4J.

    :param word:  A dict object representing a vocabulary
    :param language:  The language of the vocabulary. Can only be one of the constants defined in this file:
    :py:data:`GERMAN` / :py:data:`LATIN` / :py:data:`ANCIENT_GREEK`
    :param node_label_attribute_key:  The attribute key in the returned map whose value contains the node caption
    :param inflection_supplier:  A functional object that, given a YAML dictionary, returns the inflection table of that
    word. The key of the table can be arbitrary but the value must be a sole inflected word

    :return: a flat map containing all the YAML encoded information about the vocabulary
    """
    return {node_label_attribute_key: word["term"], "language": language} | inflection_supplier(word) | get_audio(word)


def get_audio(word: object) -> dict:
    """
    Returns the pronunciation of a word in the form of a map with key being "audio" and value being a string pointing to
    the URL of the audio file.

    The word should be a dict object containing an "audio" string attribute, otherwise this function returns an empty
    map

    :param word:  A dict object representing a vocabulary

    :return: a single-entry map or empty map
    """
    if "audio" not in word:
        return {}

    if word["audio"] == "" or word["audio"] is None:
        raise ValueError(
            "{} has an emtpy 'audio' field. Either fill it with an URL or simply remove the 'audio' field.".format(word)
        )

    return {"audio": word["audio"]}


def get_inferred_links(
        vocabulary: list[dict],
        label_key: str,
        inflection_supplier: Callable[[object], dict[str, str]] = lambda word: {}
) -> list[dict]:
    """
    Return a list of inferred links between related vocabularies.

    This function is the point of extending link inference capabilities. At this point, the link inference includes

    - :py:meth:`token sharing <huggingface.vocabulary_parser.get_inferred_tokenization_links>`
    - :py:meth:`token sharing <huggingface.vocabulary_parser.get_levenshtein_links>`

    :param vocabulary:  An Antiqua-compatible YAML file deserialized
    :param label_key:  The name of the node attribute that will be used as the label in displaying the node
    :param inflection_supplier:  A functional object that, given a YAML dictionary, returns the inflection table of that
    word. The key of the table can be arbitrary but the value must be a sole inflected word

    :return: a list of link object, each of which has a "source_label", a "target_label", and an "attributes" key
    """
    return (get_inferred_tokenization_links(vocabulary, label_key, inflection_supplier) +
            get_structurally_similar_links(vocabulary, label_key))


def get_definition_tokens(word: dict) -> set[str]:
    definitions = [pair[1] for pair in get_definitions(word)]
    tokens = set()

    for token in set(sum([definition.split(" ") for definition in set().union(set(definitions))], [])):
        cleansed = token.lower().strip().replace('(', '').replace(')', '')  # trim and remove parenthesis
        if cleansed not in EXCLUDED_DEFINITION_TOKENS:
            tokens.add(cleansed)

    return tokens


def get_term_tokens(word: dict) -> set[str]:
    term = word["term"]
    tokens = set()

    for token in term.split(" "):
        cleansed = token.lower().strip()
        if cleansed not in {"der", "die", "das"}:
            tokens.add(cleansed)

    return tokens


def get_inflection_tokens(
        word: dict,
        inflection_supplier: Callable[[object], dict[str, str]] = lambda word: {}
) -> set[str]:
    tokens = set()

    for key, value in inflection_supplier(word).items():
        if value not in EXCLUDED_INFLECTION_ENTRIES:
            for inflection in value.split(","):
                cleansed = inflection.lower().strip()
                tokens.add(cleansed)

    return tokens


def get_tokens_of(word: dict, inflection_supplier: Callable[[object], dict[str, str]] = lambda word: {}) -> set[str]:
    """
    Returns the tokens of a word used for link inferences.

    The tokens come from the following attributes:

    1. term
    2. definition
    3. inflection field (conjugation & declension)

    :param word:  A list entry of Antiqua-compatible YAML file deserialized
    :param inflection_supplier:  A functional object that, given a YAML dictionary, returns the inflection table of that
    word. The key of the table can be arbitrary but the value must be a sole inflected word

    :return: a list of tokens
    """
    return get_inflection_tokens(word, inflection_supplier) | get_term_tokens(word) | get_definition_tokens(word)


def get_inferred_tokenization_links(
        vocabulary: list[dict],
        label_key: str,
        inflection_supplier: Callable[[object], dict[str, str]] = lambda word: {}
) -> list[dict]:
    """
    Return a list of inferred links between related vocabulary terms which are related to one another.

    This mapping will be used to create more links in graph database.

    This was inspired by the spotting the relationships among::

        vocabulary:
          - term: das Jahr
            definition: the year
            declension:
              - ["",         singular,        plural        ]
              - [nominative, Jahr,            "Jahre, Jahr" ]
              - [genitive,   "Jahres, Jahrs", "Jahre, Jahr" ]
              - [dative,     Jahr,            "Jahren, Jahr"]
              - [accusative, Jahr,            "Jahre, Jahr" ]
          - term: seit zwei Jahren
            definition: for two years
          - term: in den letzten Jahren
            definition: in recent years

    1. Both 2nd and 3rd are related to the 1st and the two links can be inferred by observing that "Jahren" in 2nd and
       3rd match the declension table of the 1st
    2. In addition, the 2nd and 3rd are related because they both have "Jahren".

    Given the 2 observations above, this function tokenizes the "term" and the declension table of each word. If two
    words share at least 1 token, they are defined to be "related"

    :param vocabulary:  A Antiqua-compatible YAML file deserialized
    :param label_key:  The name of the node attribute that will be used as the label in displaying the node
    :param inflection_supplier:  A functional object that, given a YAML dictionary, returns the inflection table of that
    word. The key of the table can be arbitrary but the value must be a sole inflected word

    :return: a list of link object, each of which has a "source_label", a "target_label", and an "attributes" key
    """
    all_vocabulary_tokenizations_by_term = dict(
        [word["term"], get_tokens_of(word, inflection_supplier)] for word in vocabulary)

    existing_pairs: set[set] = set()
    inferred_links = []
    for this_word in vocabulary:
        this_term = this_word["term"]

        for that_term, that_term_tokens in all_vocabulary_tokenizations_by_term.items():
            jump_to_next_term = False

            if this_term == that_term:
                continue

            for this_token in all_vocabulary_tokenizations_by_term[this_term]:
                for that_token in that_term_tokens:
                    if this_token.lower().strip() == that_token and ({this_term, that_term} not in existing_pairs):
                        existing_pairs.add(frozenset({this_term, that_term}))

                        inferred_links.append({
                            "source_label": this_term,
                            "target_label": that_term,
                            "attributes": {label_key: "term related"},
                        })

                        jump_to_next_term = True
                        break

                if jump_to_next_term:
                    break

    return inferred_links


def get_structurally_similar_links(vocabulary: list[dict], label_key: str) -> list[dict]:
    """
    Return a list of inferred links between structurally-related vocabulary terms that are determined by the function
    :py:meth:`token sharing <huggingface.vocabulary_parser.is_structurally_similar>`.

    This was inspired by the spotting the relationships among::

        vocabulary:
          - term: anschließen
            definition: to connect
          - term: anschließend
            definition:
              - (adj.) following
              - (adv.) afterwards
          - term: nachher
            definition: (adv.) afterwards

    :param vocabulary:  A Antiqua-compatible YAML file deserialized
    :param label_key:  The name of the node attribute that will be used as the label in displaying the node

    :return: a list of link object, each of which has a "source_label", a "target_label", and an "attributes" key
    """
    inferred_links = []

    for this in vocabulary:
        for that in vocabulary:
            this_term = this["term"]
            that_term = that["term"]
            if is_structurally_similar(this_term, that_term):
                inferred_links.append({
                    "source_label": this_term,
                    "target_label": that_term,
                    "attributes": {label_key: "structurally similar"},
                })

    return inferred_links


def is_structurally_similar(this_word: str, that_word: str) -> bool:
    """
    Returns whether or not two string words are structurally similar.

    Two words are structurally similar iff the two share the same word stem. If two word strings are equal, this
    function returns `False`.

    :param this_word:  The first word to compare structurally
    :param that_word:  The second word to compare structurally

    :return: `True` if two words are structurally similar, or `False` otherwise
    """
    if this_word is that_word:
        return False

    return get_stem(this_word) == get_stem(that_word)


def get_stem(word: str) -> str:
    from nltk.stem.snowball import GermanStemmer
    stemmer = GermanStemmer()
    return stemmer.stem(word)
