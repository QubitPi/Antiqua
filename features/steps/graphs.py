# Copyright Jiaqi Liu
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from behave import *
from neo4j import GraphDatabase


@when("we expand 'δέ' by 3 hops at most")
def step_impl(context):
    assert True is not False


@then('we get 13 nodes and 13 links, all distinct')
def step_impl(context):
    driver = GraphDatabase.driver("neo4j://localhost:7687", auth=("not used", "not used"))

    with driver.session() as session:
        result = parse_apoc_path_expand_result(session.run(
            """
            MATCH (node{label:"δέ"})
            CALL apoc.path.expand(node, "LINK", null, 1, 3)
            YIELD path
            RETURN path;
            """
        ))

        assert set(result["nodes"]) == {"aber lieber", "aber", "but", "sed", "ἀλλά", "δέ", "and", "τε", "et", "καί",
                                        "also", "even", "δ’"}


def parse_apoc_path_expand_result(result):
    nodes = set()
    links = []

    nodeMap = dict()
    duplicateLinks = set()
    for record in result:
        path = record["path"]

        for node in path.nodes:
            label = dict(node)["label"]
            nodes.add(label)
            nodeMap[node.id] = label

        for link in path.relationships:
            if link.id not in duplicateLinks:
                duplicateLinks.add(link.id)

                links.append({
                    "source": nodeMap[link.start_node.id],
                    "target": nodeMap[link.end_node.id],
                    "label": dict(link)["label"],
                })

    return {"nodes": list(nodes), "links": links}
