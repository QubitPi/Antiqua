# Copyright 2025 Jiaqi Liu. All rights reserved.
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

import argparse
import sys

last_tag = ""
try:
    if len(sys.argv) < 2:
        print("Usage: python upversion.py <tag>", file=sys.stderr)
        sys.exit(1)

    parser = argparse.ArgumentParser(description='Increment the last part of a version tag.')
    parser.add_argument('tag', help='The version tag to increment.')
    args = parser.parse_args()
    last_tag = args.tag

    # Handle git-describe output like 'v0.1.0-1-g1234567' by taking the tag part
    base_tag = last_tag.split('-')[0]

    # Handle 'v' prefix if it exists
    prefix = 'v' if base_tag.startswith('v') else ''
    version_part = base_tag.lstrip('v')

    parts = version_part.split('.')
    parts[-1] = str(int(parts[-1]) + 1)

    new_version = ".".join(parts)
    print(f"{prefix}{new_version}")

except (ValueError, IndexError) as e:
    print(f"Error: Could not parse version from tag '{last_tag}': {type(e).__name__} - {e}", file=sys.stderr)
    sys.exit(1)
