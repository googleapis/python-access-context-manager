from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GcpUserAccessBinding(_message.Message):
    __slots__ = ("name", "group_key", "access_levels")
    NAME_FIELD_NUMBER: _ClassVar[int]
    GROUP_KEY_FIELD_NUMBER: _ClassVar[int]
    ACCESS_LEVELS_FIELD_NUMBER: _ClassVar[int]
    name: str
    group_key: str
    access_levels: _containers.RepeatedScalarFieldContainer[str]
    def __init__(
        self,
        name: _Optional[str] = ...,
        group_key: _Optional[str] = ...,
        access_levels: _Optional[_Iterable[str]] = ...,
    ) -> None: ...
