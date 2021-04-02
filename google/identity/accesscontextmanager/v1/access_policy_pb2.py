# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
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

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/identity/accesscontextmanager/v1/access_policy.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/identity/accesscontextmanager/v1/access_policy.proto",
    package="google.identity.accesscontextmanager.v1",
    syntax="proto3",
    serialized_options=b"\n+com.google.identity.accesscontextmanager.v1B\013PolicyProtoP\001Z[google.golang.org/genproto/googleapis/identity/accesscontextmanager/v1;accesscontextmanager\242\002\004GACM\252\002'Google.Identity.AccessContextManager.V1\312\002'Google\\Identity\\AccessContextManager\\V1\352\002*Google::Identity::AccessContextManager::V1",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b"\n;google/identity/accesscontextmanager/v1/access_policy.proto\x12'google.identity.accesscontextmanager.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\"\xab\x01\n\x0c\x41\x63\x63\x65ssPolicy\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06parent\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\x12/\n\x0b\x63reate_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04\x65tag\x18\x06 \x01(\tB\xa1\x02\n+com.google.identity.accesscontextmanager.v1B\x0bPolicyProtoP\x01Z[google.golang.org/genproto/googleapis/identity/accesscontextmanager/v1;accesscontextmanager\xa2\x02\x04GACM\xaa\x02'Google.Identity.AccessContextManager.V1\xca\x02'Google\\Identity\\AccessContextManager\\V1\xea\x02*Google::Identity::AccessContextManager::V1b\x06proto3",
    dependencies=[
        google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
    ],
)


_ACCESSPOLICY = _descriptor.Descriptor(
    name="AccessPolicy",
    full_name="google.identity.accesscontextmanager.v1.AccessPolicy",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.identity.accesscontextmanager.v1.AccessPolicy.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="parent",
            full_name="google.identity.accesscontextmanager.v1.AccessPolicy.parent",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="title",
            full_name="google.identity.accesscontextmanager.v1.AccessPolicy.title",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="create_time",
            full_name="google.identity.accesscontextmanager.v1.AccessPolicy.create_time",
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="update_time",
            full_name="google.identity.accesscontextmanager.v1.AccessPolicy.update_time",
            index=4,
            number=5,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="etag",
            full_name="google.identity.accesscontextmanager.v1.AccessPolicy.etag",
            index=5,
            number=6,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=168,
    serialized_end=339,
)

_ACCESSPOLICY.fields_by_name[
    "create_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ACCESSPOLICY.fields_by_name[
    "update_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name["AccessPolicy"] = _ACCESSPOLICY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AccessPolicy = _reflection.GeneratedProtocolMessageType(
    "AccessPolicy",
    (_message.Message,),
    {
        "DESCRIPTOR": _ACCESSPOLICY,
        "__module__": "google.identity.accesscontextmanager.v1.access_policy_pb2"
        # @@protoc_insertion_point(class_scope:google.identity.accesscontextmanager.v1.AccessPolicy)
    },
)
_sym_db.RegisterMessage(AccessPolicy)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
