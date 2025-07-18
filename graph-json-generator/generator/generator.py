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
from parser.vocabulary_parser import get_attributes
from parser.vocabulary_parser import get_definitions
from parser.vocabulary_parser import get_vocabulary


def generate(yaml_path: str, language: str) -> list:
    """
    Generates a Hugging Face Dataset from Antiqua/latin/

    :param yaml_path:  The absolute or relative path (to the invoking script) to the YAML file above
    :param dataset_path:  The absolute or relative path (to the invoking script) to the generated dataset file
    """
    vocabulary = get_vocabulary(yaml_path)
    label_key = "label"

    triples = []

    for word in vocabulary:
        attributes = get_attributes(word, language, label_key)
        source_node = attributes

        for definition_with_predicate in get_definitions(word):
            predicate = definition_with_predicate[0]
            definition = definition_with_predicate[1]

            target_node = {label_key: definition}
            label = {label_key: predicate if predicate else "definition"}

            triples.append({"source": source_node, "target": target_node, "link": label})

    return triples
