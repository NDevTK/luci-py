# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: components/auth/proto/realms.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='components/auth/proto/realms.proto',
  package='components.auth.realms',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\"components/auth/proto/realms.proto\x12\x16\x63omponents.auth.realms\"\x85\x01\n\x06Realms\x12\x13\n\x0b\x61pi_version\x18\x01 \x01(\x03\x12\x37\n\x0bpermissions\x18\x02 \x03(\x0b\x32\".components.auth.realms.Permission\x12-\n\x06realms\x18\x03 \x03(\x0b\x32\x1d.components.auth.realms.Realm\"\x1a\n\nPermission\x12\x0c\n\x04name\x18\x01 \x01(\t\"H\n\x05Realm\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x31\n\x08\x62indings\x18\x02 \x03(\x0b\x32\x1f.components.auth.realms.Binding\"2\n\x07\x42inding\x12\x13\n\x0bpermissions\x18\x01 \x03(\r\x12\x12\n\nprincipals\x18\x02 \x03(\tb\x06proto3')
)




_REALMS = _descriptor.Descriptor(
  name='Realms',
  full_name='components.auth.realms.Realms',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='api_version', full_name='components.auth.realms.Realms.api_version', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='permissions', full_name='components.auth.realms.Realms.permissions', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='realms', full_name='components.auth.realms.Realms.realms', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=63,
  serialized_end=196,
)


_PERMISSION = _descriptor.Descriptor(
  name='Permission',
  full_name='components.auth.realms.Permission',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='components.auth.realms.Permission.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=198,
  serialized_end=224,
)


_REALM = _descriptor.Descriptor(
  name='Realm',
  full_name='components.auth.realms.Realm',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='components.auth.realms.Realm.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bindings', full_name='components.auth.realms.Realm.bindings', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=226,
  serialized_end=298,
)


_BINDING = _descriptor.Descriptor(
  name='Binding',
  full_name='components.auth.realms.Binding',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='permissions', full_name='components.auth.realms.Binding.permissions', index=0,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='principals', full_name='components.auth.realms.Binding.principals', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=300,
  serialized_end=350,
)

_REALMS.fields_by_name['permissions'].message_type = _PERMISSION
_REALMS.fields_by_name['realms'].message_type = _REALM
_REALM.fields_by_name['bindings'].message_type = _BINDING
DESCRIPTOR.message_types_by_name['Realms'] = _REALMS
DESCRIPTOR.message_types_by_name['Permission'] = _PERMISSION
DESCRIPTOR.message_types_by_name['Realm'] = _REALM
DESCRIPTOR.message_types_by_name['Binding'] = _BINDING
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Realms = _reflection.GeneratedProtocolMessageType('Realms', (_message.Message,), dict(
  DESCRIPTOR = _REALMS,
  __module__ = 'components.auth.proto.realms_pb2'
  # @@protoc_insertion_point(class_scope:components.auth.realms.Realms)
  ))
_sym_db.RegisterMessage(Realms)

Permission = _reflection.GeneratedProtocolMessageType('Permission', (_message.Message,), dict(
  DESCRIPTOR = _PERMISSION,
  __module__ = 'components.auth.proto.realms_pb2'
  # @@protoc_insertion_point(class_scope:components.auth.realms.Permission)
  ))
_sym_db.RegisterMessage(Permission)

Realm = _reflection.GeneratedProtocolMessageType('Realm', (_message.Message,), dict(
  DESCRIPTOR = _REALM,
  __module__ = 'components.auth.proto.realms_pb2'
  # @@protoc_insertion_point(class_scope:components.auth.realms.Realm)
  ))
_sym_db.RegisterMessage(Realm)

Binding = _reflection.GeneratedProtocolMessageType('Binding', (_message.Message,), dict(
  DESCRIPTOR = _BINDING,
  __module__ = 'components.auth.proto.realms_pb2'
  # @@protoc_insertion_point(class_scope:components.auth.realms.Binding)
  ))
_sym_db.RegisterMessage(Binding)


# @@protoc_insertion_point(module_scope)