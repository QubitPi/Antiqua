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
import os

from neo4j import GraphDatabase

URI = os.environ["NEO4J_URI"]
DATABASE = os.environ["NEO4J_DATABASE"]
AUTH = (os.environ["NEO4J_USERNAME"], os.environ["NEO4J_PASSWORD"])


def cleanup_neo4j():
    """
    Delete all nodes and links in a specified Neo4J database.

    The database is identified by the following environment variables:

    - `NEO4J_URI`: the connection URL of the database, such as "neo4j://localhost", "neo4j+s://xxx.databases.neo4j.io"
    - `NEO4J_DATABASE`: the database name, e.g. "my_database"
    - `NEO4J_USERNAME`: the username for connecting the database
    - `NEO4J_PASSWORD`: the user's password for the connection
    """
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        driver.verify_connectivity()
        driver.execute_query("match (a) -[r] -> () delete a, r")
        driver.execute_query("match (a) delete a")
