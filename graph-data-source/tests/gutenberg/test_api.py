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

from gutenberg.api import get_book_txt_by_url
from gutenberg.api import get_unique_terms


class TestApi(unittest.TestCase):

    def test_get_unique_terms(self):
        vocabulary = get_unique_terms(get_book_txt_by_url("https://www.gutenberg.org/files/6342/6342-8.txt"))
        self.assertEqual(len(vocabulary), len(set(vocabulary)))
