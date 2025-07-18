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

from database.neo4j.database_clients import get_database_client


def is_definition_node(node):
    return "language" not in node


def load_into_neo4j(graph_json_path: str, language: str):
    with get_database_client() as database_client:
        with open(graph_json_path, "r") as graph_json:
            graph = json.load(graph_json)
            for triple in graph:
                source_node_attributes = {k: v for k, v in triple["source"].items() if v}
                database_client.save_a_node_with_attributes("Term", source_node_attributes)

                target_node_attributes = {k: v for k, v in triple["target"].items() if v}
                database_client.save_a_node_with_attributes(
                    "Definition" if is_definition_node(triple["target"]) else "Term",
                    target_node_attributes
                )

                link = triple["link"]
                database_client.save_a_link_with_attributes(
                    language=language,
                    source_label=source_node_attributes["label"],
                    target_label=target_node_attributes["label"],
                    attributes=link
                )
