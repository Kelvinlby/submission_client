from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MessageData(_message.Message):
    __slots__ = ("command", "name", "value")
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    command: int
    name: str
    value: float
    def __init__(self, command: _Optional[int] = ..., name: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...

class ReturnData(_message.Message):
    __slots__ = ("ret",)
    RET_FIELD_NUMBER: _ClassVar[int]
    ret: int
    def __init__(self, ret: _Optional[int] = ...) -> None: ...
