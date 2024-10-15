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

from multiprocessing import Process, Queue

from wilhelm_python_sdk import latin_loader
from wilhelm_python_sdk import german_loader
from wilhelm_python_sdk import ancient_greek_loader

def load_latin(queue):
    latin_loader.load_into_database("latin.yaml")
    queue.put("Latin loads successfully")


def load_german(queue):
    german_loader.load_into_database("german.yaml")
    queue.put("German loads successfully")


def load_ancient_greek(queue):
    ancient_greek_loader.load_into_database("ancient_greek.yaml")
    queue.put("Ancient Greek loads successfully")


if __name__ == "__main__":
    queue = Queue()

    latin = Process(target=load_latin, args=(queue, ))
    german = Process(target=load_german, args=(queue, ))
    ancient_greek = Process(target=load_ancient_greek, args=(queue, ))

    latin.start()
    german.start()
    ancient_greek.start()

    # Blocking
    result = queue.get()
