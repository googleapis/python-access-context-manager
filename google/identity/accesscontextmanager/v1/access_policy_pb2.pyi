from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import (
    ClassVar as _ClassVar,
    Iterable as _Iterable,
    Mapping as _Mapping,
    Optional as _Optional,
    Union as _Union,
)

DESCRIPTOR: _descriptor.FileDescriptor

class AccessPolicy(_message.Message):
    __slots__ = (
        "name",
        "parent",
        "title",
        "scopes",
        "create_time",
        "update_time",
        "etag",
    )
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    parent: str
    title: str
    scopes: _containers.RepeatedScalarFieldContainer[str]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    etag: str
    def __init__(
        self,
        name: _Optional[str] = ...,
        parent: _Optional[str] = ...,
        title: _Optional[str] = ...,
        scopes: _Optional[_Iterable[str]] = ...,
        create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        etag: _Optional[str] = ...,
    ) -> None: ...
