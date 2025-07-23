#!/bin/bash
set -x
set -e

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

mkdir anki-decks
cd anki-decks

pip3 install lexitheras
printf "1\n" | lexitheras Iliad

docker run -d -p 8529:8529 -e ARANGO_NO_AUTH=1 jack20191124/wiktionary-data &
# shellcheck disable=SC2034,SC2015
for i in {1..60}; do
  curl -vL http://localhost:8529 && break || sleep 1
done

cd ../graph-data-source
pip3 install -r requirements.txt
pip3 install -e .
cd gutenberg
python3 api.py

mv *.apkg ../../anki-decks/
