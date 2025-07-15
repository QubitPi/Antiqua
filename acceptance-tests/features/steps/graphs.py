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

from behave import then
from behave import when
from hamcrest import assert_that
from hamcrest import equal_to
from neo4j import GraphDatabase

# Set up the logging
logging.basicConfig(level=logging.INFO)
neo4j_logger = logging.getLogger("neo4j")
neo4j_logger.setLevel(logging.DEBUG)  # Log all queries


@when('we expand "{term}" by {num_hops:d} hops at most')
def step_impl(context, term, num_hops):
    driver = GraphDatabase.driver("neo4j://localhost:7687", auth=("not used", "not used"))

    with driver.session() as session:
        context.result = parse_apoc_path_expand_result(session.run(
            """
                MATCH (node{label:$term})
                CALL apoc.path.expand(node, "LINK", null, 1, $num_hops)
                YIELD path
                RETURN path;
            """,
            term=term,
            num_hops=num_hops
        ))


@then('we get these distinct nodes: {nodes}')
def step_impl(context, nodes):
    assert_that(set(context.result["nodes"]), equal_to(eval(nodes)))


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
