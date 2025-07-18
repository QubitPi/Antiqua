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
import unittest
from parser.vocabulary_parser import GERMAN

from generator.generator import generate


class TestGenerator(unittest.TestCase):

    def test_generate(self):
        from pathlib import Path
        script_dir = Path(__file__).parent
        test_yaml = "test.yaml"
        full_path = script_dir / test_yaml
        self.assertEqual(
            [
                {
                    'source': {'label': 'null', 'language': 'German'},
                    'target': {'label': '0'},
                    'link': {'label': 'definition'},
                },
                {
                    'source': {'label': 'eins', 'language': 'German'},
                    'target': {'label': '1'},
                    'link': {'label': 'definition'},
                },
                {
                    'source': {'label': 'Guten Tag', 'language': 'German'},
                    'target': {'label': 'Good day'},
                    'link': {'label': 'definition'},
                },
                {
                    'source': {'label': 'Hallo', 'language': 'German'},
                    'target': {'label': 'Hello'},
                    'link': {'label': 'definition'}
                }
            ],
            generate(full_path, GERMAN)
        )
