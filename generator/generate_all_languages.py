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
import generate_ancient_greek
import generate_german
import generate_latin

if __name__ == "__main__":
    generate_german.generate("../german.yaml", "./german-graph-data.json")
    generate_latin.generate("../latin.yaml", "./latin-graph-data.json")
    generate_ancient_greek.generate("../ancient-greek.yaml", "./ancient-greek-graph-data.json")
