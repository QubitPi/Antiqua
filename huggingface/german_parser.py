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


def get_declension_attributes(word: object) -> dict[str, str]:
    """
    Returns the declension of a word.

    If the word does not have a "declension" field or the noun's declension is, for some reasons, "Unknown", this
    function returns an empty dictionary.

    The declension table is flattened with "declension index" as the map key and the declined form as map value.
    Specifically:

    - A regular noun declension with a map structure of::

          term: der Hut
          definition: the hat
          declension:
            - ["",         singular,      plural]
            - [nominative, Hut,           Hüte  ]
            - [genitive,   "Hutes, Huts", Hüte  ]
            - [dative,     Hut,           Hüten ]
            - [accusative, Hut,           Hüte  ]

      The returned map would be::

          {
              "declension-0-0": "",
              "declension-0-1": "singular",
              "declension-0-2": "plural",
              "declension-1-0": "nominative",
              "declension-1-1": "Hut",
              "declension-1-2": "Hüte",
              ...
          }

    - A adjectival declension with a map structure of::

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

      The returned map would be::

        {
            'strong-0-0': '',
            'strong-0-1': 'singular',
            'strong-0-2': 'plural',
            'strong-1-0': 'nominative',
            'strong-1-1': 'Gefangener',
            'strong-1-2': 'Gefangene',
            ...
        }

    :param word:  A vocabulary represented in YAML dictionary which has a "declension" key

    :return: a flat map containing all the YAML encoded information about the noun excluding term and definition
    """

    if "declension" not in word:
        return {}

    declension = word["declension"]

    if declension == "Unknown":
        return {}

    declension_tables = {}
    if "strong" in declension and "weak" in declension and "mixed" in declension:
        declension_tables["strong"] = declension["strong"]
        declension_tables["weak"] = declension["weak"]
        declension_tables["mixed"] = declension["mixed"]
    else:
        declension_tables["declension"] = declension

    declension_attributes = {}
    for declension_type, declension_table in declension_tables.items():
        for i, row in enumerate(declension_table):
            for j, col in enumerate(row):
                declension_attributes[f"{declension_type}-{i}-{j}"] = declension_table[i][j]

    return declension_attributes
