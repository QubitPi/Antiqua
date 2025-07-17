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
import generate_ancient_greek_dataset
import generate_german_dataset
import generate_latin_dataset

if __name__ == "__main__":
    generate_german_dataset.generate_dataset("../german.yaml", "../german-graph-data.jsonl")
    generate_german_dataset.generate_dataset("../italian/italian.yaml", "../italian-graph-data.jsonl")
    generate_latin_dataset.generate_dataset("../latin.yaml", "../latin-graph-data.jsonl")
    generate_ancient_greek_dataset.generate_dataset("../ancient-greek.yaml", "../ancient-greek-graph-data.jsonl")
