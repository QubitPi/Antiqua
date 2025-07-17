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

from database.neo4j.database_clients import get_node_label_attribute_key
from vocabulary_parser import ANCIENT_GREEK
from vocabulary_parser import get_attributes
from vocabulary_parser import get_definitions
from vocabulary_parser import get_vocabulary


def generate_dataset(yaml_path: str, dataset_path: str):
    """
    Generates a Hugging Face Dataset from ../ancient-greek

    :param yaml_path:  The absolute or relative path (to the invoking script) to the YAML file above
    :param dataset_path:  The absolute or relative path (to the invoking script) to the generated dataset file
    """
    vocabulary = get_vocabulary(yaml_path)
    label_key = get_node_label_attribute_key()

    all_nodes = {}

    with open(dataset_path, "w") as graph:
        for word in vocabulary:
            term = word["term"]
            attributes = get_attributes(word, ANCIENT_GREEK, label_key)
            source_node = attributes

            all_nodes[term] = source_node

            for definition_with_predicate in get_definitions(word):
                predicate = definition_with_predicate[0]
                definition = definition_with_predicate[1]

                target_node = {label_key: definition}
                label = {label_key: predicate if predicate else "definition"}

                graph.write(json.dumps({"source": source_node, "target": target_node, "link": label}))
                graph.write("\n")
