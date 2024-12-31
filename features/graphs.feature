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
Feature: Neo4J in Docker shows expected graphs

  Scenario Outline: Vocabulary Linking
    When we expand "<term>" by <hops> hops at most
    Then we get these distinct nodes: <nodes>

    Examples: Ancient Greek
      | term | hops | nodes                                                                                               |
      | δέ   | 3    | {"aber lieber", "aber", "but", "sed", "ἀλλά", "δέ", "and", "τε", "et", "καί", "also", "even", "δ᾽"} |
