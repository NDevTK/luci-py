# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service_config.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='service_config.proto',
  package='luci.config',
  serialized_pb='\n\x14service_config.proto\x12\x0bluci.config\"&\n\x06\x41\x63lCfg\x12\x1c\n\x14service_access_group\x18\x01 \x01(\t\"\x83\x01\n\tImportCfg\x12/\n\x07gitiles\x18\x01 \x01(\x0b\x32\x1e.luci.config.ImportCfg.Gitiles\x1a\x45\n\x07Gitiles\x12\x1a\n\x12\x66\x65tch_log_deadline\x18\x01 \x01(\x05\x12\x1e\n\x16\x66\x65tch_archive_deadline\x18\x02 \x01(\x05')




_ACLCFG = _descriptor.Descriptor(
  name='AclCfg',
  full_name='luci.config.AclCfg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='service_access_group', full_name='luci.config.AclCfg.service_access_group', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=37,
  serialized_end=75,
)


_IMPORTCFG_GITILES = _descriptor.Descriptor(
  name='Gitiles',
  full_name='luci.config.ImportCfg.Gitiles',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fetch_log_deadline', full_name='luci.config.ImportCfg.Gitiles.fetch_log_deadline', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fetch_archive_deadline', full_name='luci.config.ImportCfg.Gitiles.fetch_archive_deadline', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=140,
  serialized_end=209,
)

_IMPORTCFG = _descriptor.Descriptor(
  name='ImportCfg',
  full_name='luci.config.ImportCfg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gitiles', full_name='luci.config.ImportCfg.gitiles', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_IMPORTCFG_GITILES, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=78,
  serialized_end=209,
)

_IMPORTCFG_GITILES.containing_type = _IMPORTCFG;
_IMPORTCFG.fields_by_name['gitiles'].message_type = _IMPORTCFG_GITILES
DESCRIPTOR.message_types_by_name['AclCfg'] = _ACLCFG
DESCRIPTOR.message_types_by_name['ImportCfg'] = _IMPORTCFG

class AclCfg(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ACLCFG

  # @@protoc_insertion_point(class_scope:luci.config.AclCfg)

class ImportCfg(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType

  class Gitiles(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _IMPORTCFG_GITILES

    # @@protoc_insertion_point(class_scope:luci.config.ImportCfg.Gitiles)
  DESCRIPTOR = _IMPORTCFG

  # @@protoc_insertion_point(class_scope:luci.config.ImportCfg)


# @@protoc_insertion_point(module_scope)
