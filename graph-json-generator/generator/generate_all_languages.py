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
from parser.vocabulary_parser import ANCIENT_GREEK
from parser.vocabulary_parser import ITALIAN
from parser.vocabulary_parser import LATIN

import generate_german
from generator import generate

if __name__ == "__main__":
    for yaml_input_file, json_output_file, language in [
        ("../../graph-data-source/latin/latin.yaml", "../latin-graph-data.json", LATIN),
        ("../../graph-data-source/italian/italian.yaml", "../italian-graph-data.json", ITALIAN),
        ("../../graph-data-source/ancient-greek/ancient-greek.yaml", "../ancient-greek-graph-data.json", ANCIENT_GREEK),
    ]:
        with open(json_output_file, "w", encoding="utf-8") as json_file:
            json.dump(generate(yaml_input_file, language), json_file, ensure_ascii=False, indent=4)

    generate_german.generate("../../graph-data-source/german/german.yaml", "../german-graph-data.json")
