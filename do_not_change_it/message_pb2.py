# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='message.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rmessage.proto\"\x7f\n\x03Msg\x12\x16\n\x04type\x18\x01 \x01(\x0e\x32\x08.MsgType\x12\x17\n\x05login\x18\x02 \x01(\x0b\x32\x06.LoginH\x00\x12\x1c\n\x08login_ok\x18\x03 \x01(\x0b\x32\x08.LoginOkH\x00\x12 \n\nlogin_fail\x18\x04 \x01(\x0b\x32\n.LoginFailH\x00\x42\x07\n\x05union\"\x15\n\x05Login\x12\x0c\n\x04name\x18\x01 \x01(\t\"\t\n\x07LoginOk\"\x0b\n\tLoginFail*3\n\x07MsgType\x12\n\n\x06TLogin\x10\x00\x12\x0c\n\x08TLoginOk\x10\x01\x12\x0e\n\nTLoginFail\x10\x02\x62\x06proto3'
)

_MSGTYPE = _descriptor.EnumDescriptor(
  name='MsgType',
  full_name='MsgType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TLogin', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TLoginOk', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TLoginFail', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=193,
  serialized_end=244,
)
_sym_db.RegisterEnumDescriptor(_MSGTYPE)

MsgType = enum_type_wrapper.EnumTypeWrapper(_MSGTYPE)
TLogin = 0
TLoginOk = 1
TLoginFail = 2



_MSG = _descriptor.Descriptor(
  name='Msg',
  full_name='Msg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Msg.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='login', full_name='Msg.login', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='login_ok', full_name='Msg.login_ok', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='login_fail', full_name='Msg.login_fail', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='union', full_name='Msg.union',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=17,
  serialized_end=144,
)


_LOGIN = _descriptor.Descriptor(
  name='Login',
  full_name='Login',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Login.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=146,
  serialized_end=167,
)


_LOGINOK = _descriptor.Descriptor(
  name='LoginOk',
  full_name='LoginOk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=169,
  serialized_end=178,
)


_LOGINFAIL = _descriptor.Descriptor(
  name='LoginFail',
  full_name='LoginFail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=180,
  serialized_end=191,
)

_MSG.fields_by_name['type'].enum_type = _MSGTYPE
_MSG.fields_by_name['login'].message_type = _LOGIN
_MSG.fields_by_name['login_ok'].message_type = _LOGINOK
_MSG.fields_by_name['login_fail'].message_type = _LOGINFAIL
_MSG.oneofs_by_name['union'].fields.append(
  _MSG.fields_by_name['login'])
_MSG.fields_by_name['login'].containing_oneof = _MSG.oneofs_by_name['union']
_MSG.oneofs_by_name['union'].fields.append(
  _MSG.fields_by_name['login_ok'])
_MSG.fields_by_name['login_ok'].containing_oneof = _MSG.oneofs_by_name['union']
_MSG.oneofs_by_name['union'].fields.append(
  _MSG.fields_by_name['login_fail'])
_MSG.fields_by_name['login_fail'].containing_oneof = _MSG.oneofs_by_name['union']
DESCRIPTOR.message_types_by_name['Msg'] = _MSG
DESCRIPTOR.message_types_by_name['Login'] = _LOGIN
DESCRIPTOR.message_types_by_name['LoginOk'] = _LOGINOK
DESCRIPTOR.message_types_by_name['LoginFail'] = _LOGINFAIL
DESCRIPTOR.enum_types_by_name['MsgType'] = _MSGTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Msg = _reflection.GeneratedProtocolMessageType('Msg', (_message.Message,), {
  'DESCRIPTOR' : _MSG,
  '__module__' : 'message_pb2'
  # @@protoc_insertion_point(class_scope:Msg)
  })
_sym_db.RegisterMessage(Msg)

Login = _reflection.GeneratedProtocolMessageType('Login', (_message.Message,), {
  'DESCRIPTOR' : _LOGIN,
  '__module__' : 'message_pb2'
  # @@protoc_insertion_point(class_scope:Login)
  })
_sym_db.RegisterMessage(Login)

LoginOk = _reflection.GeneratedProtocolMessageType('LoginOk', (_message.Message,), {
  'DESCRIPTOR' : _LOGINOK,
  '__module__' : 'message_pb2'
  # @@protoc_insertion_point(class_scope:LoginOk)
  })
_sym_db.RegisterMessage(LoginOk)

LoginFail = _reflection.GeneratedProtocolMessageType('LoginFail', (_message.Message,), {
  'DESCRIPTOR' : _LOGINFAIL,
  '__module__' : 'message_pb2'
  # @@protoc_insertion_point(class_scope:LoginFail)
  })
_sym_db.RegisterMessage(LoginFail)


# @@protoc_insertion_point(module_scope)