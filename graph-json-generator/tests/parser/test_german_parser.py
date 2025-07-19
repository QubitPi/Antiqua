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
import unittest
from parser.german_parser import get_declension_attributes

import yaml


class TestGermanParser(unittest.TestCase):

    def test_get_declension_attributes_on_regular_noun(self):
        hut_yaml = """
            term: der Hut
            definition: the hat
            declension:
              - ["",         singular,      plural]
              - [nominative, Hut,           Hüte  ]
              - [genitive,   "Hutes, Huts", Hüte  ]
              - [dative,     Hut,           Hüten ]
              - [accusative, Hut,           Hüte  ]
        """

        expected_declension_map = {
            "declension-0-0": "",
            "declension-0-1": "singular",
            "declension-0-2": "plural",

            "declension-1-0": "nominative",
            "declension-1-1": "Hut",
            "declension-1-2": "Hüte",

            "declension-2-0": "genitive",
            "declension-2-1": "Hutes, Huts",
            "declension-2-2": "Hüte",

            "declension-3-0": "dative",
            "declension-3-1": "Hut",
            "declension-3-2": "Hüten",

            "declension-4-0": "accusative",
            "declension-4-1": "Hut",
            "declension-4-2": "Hüte",
        }

        self.assertEqual(expected_declension_map, get_declension_attributes(yaml.safe_load(hut_yaml)))

    def test_get_declension_attributes_on_adjectival(self):
        word_yaml = """
            term: der Gefangener
            definition: (adjectival, male) the prisoner
            declension:
              strong:
                - ["",         singular,   plural    ]
                - [nominative, Gefangener, Gefangene ]
                - [genitive,   Gefangenen, Gefangener]
                - [dative,     Gefangenem, Gefangenen]
                - [accusative, Gefangenen, Gefangene ]
              weak:
                - ["",         singular,   plural    ]
                - [nominative, Gefangene,  Gefangenen]
                - [genitive,   Gefangenen, Gefangenen]
                - [dative,     Gefangenen, Gefangenen]
                - [accusative, Gefangenen, Gefangenen]
              mixed:
                - ["",         singular,   plural    ]
                - [nominative, Gefangener, Gefangenen]
                - [genitive,   Gefangenen, Gefangenen]
                - [dative,     Gefangenen, Gefangenen]
                - [accusative, Gefangenen, Gefangenen]
        """

        self.assertEqual(
            {
                'mixed-0-0': '',
                'mixed-0-1': 'singular',
                'mixed-0-2': 'plural',
                'mixed-1-0': 'nominative',
                'mixed-1-1': 'Gefangener',
                'mixed-1-2': 'Gefangenen',
                'mixed-2-0': 'genitive',
                'mixed-2-1': 'Gefangenen',
                'mixed-2-2': 'Gefangenen',
                'mixed-3-0': 'dative',
                'mixed-3-1': 'Gefangenen',
                'mixed-3-2': 'Gefangenen',
                'mixed-4-0': 'accusative',
                'mixed-4-1': 'Gefangenen',
                'mixed-4-2': 'Gefangenen',
                'strong-0-0': '',
                'strong-0-1': 'singular',
                'strong-0-2': 'plural',
                'strong-1-0': 'nominative',
                'strong-1-1': 'Gefangener',
                'strong-1-2': 'Gefangene',
                'strong-2-0': 'genitive',
                'strong-2-1': 'Gefangenen',
                'strong-2-2': 'Gefangener',
                'strong-3-0': 'dative',
                'strong-3-1': 'Gefangenem',
                'strong-3-2': 'Gefangenen',
                'strong-4-0': 'accusative',
                'strong-4-1': 'Gefangenen',
                'strong-4-2': 'Gefangene',
                'weak-0-0': '',
                'weak-0-1': 'singular',
                'weak-0-2': 'plural',
                'weak-1-0': 'nominative',
                'weak-1-1': 'Gefangene',
                'weak-1-2': 'Gefangenen',
                'weak-2-0': 'genitive',
                'weak-2-1': 'Gefangenen',
                'weak-2-2': 'Gefangenen',
                'weak-3-0': 'dative',
                'weak-3-1': 'Gefangenen',
                'weak-3-2': 'Gefangenen',
                'weak-4-0': 'accusative',
                'weak-4-1': 'Gefangenen',
                'weak-4-2': 'Gefangenen'
            },
            get_declension_attributes(yaml.safe_load(word_yaml))
        )
