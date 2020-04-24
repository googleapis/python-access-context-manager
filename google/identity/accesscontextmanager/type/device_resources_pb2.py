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
# source: google/identity/accesscontextmanager/type/device_resources.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/identity/accesscontextmanager/type/device_resources.proto",
    package="google.identity.accesscontextmanager.type",
    syntax="proto3",
    serialized_options=b"\n-com.google.identity.accesscontextmanager.typeB\tTypeProtoP\001ZMgoogle.golang.org/genproto/googleapis/identity/accesscontextmanager/type;type\252\002)Google.Identity.AccessContextManager.Type\312\002)Google\\Identity\\AccessContextManager\\Type\352\002,Google::Identity::AccessContextManager::Type",
    serialized_pb=b"\n@google/identity/accesscontextmanager/type/device_resources.proto\x12)google.identity.accesscontextmanager.type\x1a\x1cgoogle/api/annotations.proto*p\n\x16\x44\x65viceEncryptionStatus\x12\x1a\n\x16\x45NCRYPTION_UNSPECIFIED\x10\x00\x12\x1a\n\x16\x45NCRYPTION_UNSUPPORTED\x10\x01\x12\x0f\n\x0bUNENCRYPTED\x10\x02\x12\r\n\tENCRYPTED\x10\x03*\x82\x01\n\x06OsType\x12\x12\n\x0eOS_UNSPECIFIED\x10\x00\x12\x0f\n\x0b\x44\x45SKTOP_MAC\x10\x01\x12\x13\n\x0f\x44\x45SKTOP_WINDOWS\x10\x02\x12\x11\n\rDESKTOP_LINUX\x10\x03\x12\x15\n\x11\x44\x45SKTOP_CHROME_OS\x10\x06\x12\x0b\n\x07\x41NDROID\x10\x04\x12\x07\n\x03IOS\x10\x05*V\n\x15\x44\x65viceManagementLevel\x12\x1a\n\x16MANAGEMENT_UNSPECIFIED\x10\x00\x12\x08\n\x04NONE\x10\x01\x12\t\n\x05\x42\x41SIC\x10\x02\x12\x0c\n\x08\x43OMPLETE\x10\x03\x42\x92\x02\n-com.google.identity.accesscontextmanager.typeB\tTypeProtoP\x01ZMgoogle.golang.org/genproto/googleapis/identity/accesscontextmanager/type;type\xaa\x02)Google.Identity.AccessContextManager.Type\xca\x02)Google\\Identity\\AccessContextManager\\Type\xea\x02,Google::Identity::AccessContextManager::Typeb\x06proto3",
    dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR],
)

_DEVICEENCRYPTIONSTATUS = _descriptor.EnumDescriptor(
    name="DeviceEncryptionStatus",
    full_name="google.identity.accesscontextmanager.type.DeviceEncryptionStatus",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="ENCRYPTION_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="ENCRYPTION_UNSUPPORTED",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="UNENCRYPTED", index=2, number=2, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="ENCRYPTED", index=3, number=3, serialized_options=None, type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=141,
    serialized_end=253,
)
_sym_db.RegisterEnumDescriptor(_DEVICEENCRYPTIONSTATUS)

DeviceEncryptionStatus = enum_type_wrapper.EnumTypeWrapper(_DEVICEENCRYPTIONSTATUS)
_OSTYPE = _descriptor.EnumDescriptor(
    name="OsType",
    full_name="google.identity.accesscontextmanager.type.OsType",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="OS_UNSPECIFIED", index=0, number=0, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="DESKTOP_MAC", index=1, number=1, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="DESKTOP_WINDOWS",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="DESKTOP_LINUX", index=3, number=3, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="DESKTOP_CHROME_OS",
            index=4,
            number=6,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="ANDROID", index=5, number=4, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="IOS", index=6, number=5, serialized_options=None, type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=256,
    serialized_end=386,
)
_sym_db.RegisterEnumDescriptor(_OSTYPE)

OsType = enum_type_wrapper.EnumTypeWrapper(_OSTYPE)
_DEVICEMANAGEMENTLEVEL = _descriptor.EnumDescriptor(
    name="DeviceManagementLevel",
    full_name="google.identity.accesscontextmanager.type.DeviceManagementLevel",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="MANAGEMENT_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="NONE", index=1, number=1, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="BASIC", index=2, number=2, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="COMPLETE", index=3, number=3, serialized_options=None, type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=388,
    serialized_end=474,
)
_sym_db.RegisterEnumDescriptor(_DEVICEMANAGEMENTLEVEL)

DeviceManagementLevel = enum_type_wrapper.EnumTypeWrapper(_DEVICEMANAGEMENTLEVEL)
ENCRYPTION_UNSPECIFIED = 0
ENCRYPTION_UNSUPPORTED = 1
UNENCRYPTED = 2
ENCRYPTED = 3
OS_UNSPECIFIED = 0
DESKTOP_MAC = 1
DESKTOP_WINDOWS = 2
DESKTOP_LINUX = 3
DESKTOP_CHROME_OS = 6
ANDROID = 4
IOS = 5
MANAGEMENT_UNSPECIFIED = 0
NONE = 1
BASIC = 2
COMPLETE = 3


DESCRIPTOR.enum_types_by_name["DeviceEncryptionStatus"] = _DEVICEENCRYPTIONSTATUS
DESCRIPTOR.enum_types_by_name["OsType"] = _OSTYPE
DESCRIPTOR.enum_types_by_name["DeviceManagementLevel"] = _DEVICEMANAGEMENTLEVEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
