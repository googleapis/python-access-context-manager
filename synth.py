# Copyright 2020 Google LLC
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

import synthtool as s
import synthtool.gcp as gcp
from synthtool import tmp
from synthtool.languages import python
from synthtool.sources import git

versions = ["v1"]

gapic = gcp.GAPICBazel()

for version in versions:
    types = gapic.py_library(
        service = "accesscontextmanager-types",
        version="types",
        proto_path=f"google/identity/accesscontextmanager/type",
        bazel_target=f"//google/identity/accesscontextmanager/type:accesscontextmanager-type-py",
    )
    s.copy(
        types / "google/cloud",
        excludes=["__init__.py"]
    )
    library = gapic.py_library(
        service = "accesscontextmanager",
        version="v1",
        proto_path=f"google/identity/accesscontextmanager/{version}",
        bazel_target=f"//google/identity/accesscontextmanager/{version}:accesscontextmanager-{version}-py",
    )
    s.copy(
        library / "google/cloud",
        excludes=["__init__.py"]
    )



# s.replace("google/**/access_level_pb2.py",
# "google\.cloud\.identity_accesscontextmanager_v1\.proto",
# "google.cloud.identity.accesscontextmanager.v1")

# ----------------------------------------------------------------------------
#  Add templated files
# ----------------------------------------------------------------------------
common = gcp.CommonTemplates()
templated_files = common.py_library()
s.move(
    templated_files, excludes=["noxfile.py", ".coveragerc", ".gitignore",],
)

s.shell.run(["nox", "-s", "blacken"], hide_output=False)

# Add license headers
python.fix_pb2_headers()
python.fix_pb2_grpc_headers()
