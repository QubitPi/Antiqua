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
import json
from parser.german_parser import get_declension_attributes
from parser.vocabulary_parser import GERMAN
from parser.vocabulary_parser import get_attributes
from parser.vocabulary_parser import get_definitions
from parser.vocabulary_parser import get_inferred_links
from parser.vocabulary_parser import get_vocabulary


def generate(yaml_path: str, dataset_path: str):
    """
    Generates a Hugging Face Dataset from Antiqua/german/

    :param yaml_path:  The absolute or relative path (to the invoking script) to the YAML file above
    :param dataset_path:  The absolute or relative path (to the invoking script) to the generated dataset file
    """
    vocabulary = get_vocabulary(yaml_path)
    label_key = "label"

    triples = []
    all_nodes = {}
    for word in vocabulary:
        term = word["term"]
        attributes = get_attributes(word, GERMAN, label_key, get_declension_attributes)
        source_node = attributes
        all_nodes[term] = source_node

        for definition_with_predicate in get_definitions(word):
            predicate = definition_with_predicate[0]
            definition = definition_with_predicate[1]

            target_node = {label_key: definition}
            label = {label_key: predicate if predicate else "definition"}

            triples.append({"source": source_node, "target": target_node, "link": label})

    for link in get_inferred_links(vocabulary, label_key, get_declension_attributes):
        source_node = all_nodes[link["source_label"]]
        target_node = all_nodes[link["target_label"]]
        label = link["attributes"]

        triples.append({"source": source_node, "target": target_node, "link": label})

    with open(dataset_path, "w") as graph:
        json.dump(triples, graph, ensure_ascii=False, indent=4)
