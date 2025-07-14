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
from datasets import load_dataset

from database.neo4j.database_clients import get_database_client

splitToLanguage = {
    "German": "German",
    "Latin": "Latin",
    "AncientGreek": "Ancient Greek"
}


def is_definition_node(node):
    return node["language"] is None


def load_into_database_by_split(split: str):
    dataset = load_dataset("QubitPi/wilhelm-vocabulary")

    with get_database_client() as database_client:
        graph = dataset[split].iter(batch_size=1)
        for triple in graph:
            source_node_attributes = {k: v for k, v in triple["source"][0].items() if v}
            database_client.save_a_node_with_attributes("Term", source_node_attributes)

            target_node_attributes = {k: v for k, v in triple["target"][0].items() if v}
            database_client.save_a_node_with_attributes(
                "Definition" if is_definition_node(triple["target"][0]) else "Term",
                target_node_attributes
            )

            link = triple["link"][0]
            database_client.save_a_link_with_attributes(
                language=splitToLanguage[split],
                source_label=source_node_attributes["label"],
                target_label=target_node_attributes["label"],
                attributes=link
            )


def load_into_database():
    load_into_database_by_split("German")


if __name__ == "__main__":
    load_into_database()
