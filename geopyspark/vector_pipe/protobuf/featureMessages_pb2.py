# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: featureMessages.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='featureMessages.proto',
  package='protos',
  syntax='proto3',
  serialized_pb=_b('\n\x15\x66\x65\x61tureMessages.proto\x12\x06protos\"E\n\x0cProtoFeature\x12\x0c\n\x04geom\x18\x01 \x01(\x0c\x12\'\n\x08metadata\x18\x02 \x01(\x0b\x32\x15.protos.ProtoMetadata\"\xb5\x01\n\rProtoMetadata\x12\n\n\x02id\x18\x01 \x01(\x06\x12\x0c\n\x04user\x18\x02 \x01(\t\x12\x0b\n\x03uid\x18\x03 \x01(\x03\x12\x11\n\tchangeset\x18\x04 \x01(\x03\x12\x0f\n\x07version\x18\x05 \x01(\x03\x12\x14\n\x0cminorVersion\x18\x06 \x01(\x03\x12\x11\n\ttimestamp\x18\x07 \x01(\t\x12\x0f\n\x07visible\x18\x08 \x01(\x08\x12\x1f\n\x04tags\x18\t \x01(\x0b\x32\x11.protos.ProtoTags\"+\n\tProtoTags\x12\x1e\n\x04tags\x18\x01 \x03(\x0b\x32\x10.protos.ProtoTag\"&\n\x08ProtoTag\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"P\n\x15ProtoFeatureCellValue\x12\x0c\n\x04geom\x18\x01 \x01(\x0c\x12)\n\tcellValue\x18\x02 \x01(\x0b\x32\x16.protos.ProtoCellValue\"/\n\x0eProtoCellValue\x12\r\n\x05value\x18\x01 \x01(\x01\x12\x0e\n\x06zindex\x18\x02 \x01(\x01\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PROTOFEATURE = _descriptor.Descriptor(
  name='ProtoFeature',
  full_name='protos.ProtoFeature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='geom', full_name='protos.ProtoFeature.geom', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='protos.ProtoFeature.metadata', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=102,
)


_PROTOMETADATA = _descriptor.Descriptor(
  name='ProtoMetadata',
  full_name='protos.ProtoMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='protos.ProtoMetadata.id', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user', full_name='protos.ProtoMetadata.user', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uid', full_name='protos.ProtoMetadata.uid', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='changeset', full_name='protos.ProtoMetadata.changeset', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='protos.ProtoMetadata.version', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='minorVersion', full_name='protos.ProtoMetadata.minorVersion', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='protos.ProtoMetadata.timestamp', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='visible', full_name='protos.ProtoMetadata.visible', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tags', full_name='protos.ProtoMetadata.tags', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=105,
  serialized_end=286,
)


_PROTOTAGS = _descriptor.Descriptor(
  name='ProtoTags',
  full_name='protos.ProtoTags',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tags', full_name='protos.ProtoTags.tags', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=288,
  serialized_end=331,
)


_PROTOTAG = _descriptor.Descriptor(
  name='ProtoTag',
  full_name='protos.ProtoTag',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='protos.ProtoTag.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='protos.ProtoTag.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=333,
  serialized_end=371,
)


_PROTOFEATURECELLVALUE = _descriptor.Descriptor(
  name='ProtoFeatureCellValue',
  full_name='protos.ProtoFeatureCellValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='geom', full_name='protos.ProtoFeatureCellValue.geom', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cellValue', full_name='protos.ProtoFeatureCellValue.cellValue', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=373,
  serialized_end=453,
)


_PROTOCELLVALUE = _descriptor.Descriptor(
  name='ProtoCellValue',
  full_name='protos.ProtoCellValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='protos.ProtoCellValue.value', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='zindex', full_name='protos.ProtoCellValue.zindex', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=455,
  serialized_end=502,
)

_PROTOFEATURE.fields_by_name['metadata'].message_type = _PROTOMETADATA
_PROTOMETADATA.fields_by_name['tags'].message_type = _PROTOTAGS
_PROTOTAGS.fields_by_name['tags'].message_type = _PROTOTAG
_PROTOFEATURECELLVALUE.fields_by_name['cellValue'].message_type = _PROTOCELLVALUE
DESCRIPTOR.message_types_by_name['ProtoFeature'] = _PROTOFEATURE
DESCRIPTOR.message_types_by_name['ProtoMetadata'] = _PROTOMETADATA
DESCRIPTOR.message_types_by_name['ProtoTags'] = _PROTOTAGS
DESCRIPTOR.message_types_by_name['ProtoTag'] = _PROTOTAG
DESCRIPTOR.message_types_by_name['ProtoFeatureCellValue'] = _PROTOFEATURECELLVALUE
DESCRIPTOR.message_types_by_name['ProtoCellValue'] = _PROTOCELLVALUE

ProtoFeature = _reflection.GeneratedProtocolMessageType('ProtoFeature', (_message.Message,), dict(
  DESCRIPTOR = _PROTOFEATURE,
  __module__ = 'featureMessages_pb2'
  # @@protoc_insertion_point(class_scope:protos.ProtoFeature)
  ))
_sym_db.RegisterMessage(ProtoFeature)

ProtoMetadata = _reflection.GeneratedProtocolMessageType('ProtoMetadata', (_message.Message,), dict(
  DESCRIPTOR = _PROTOMETADATA,
  __module__ = 'featureMessages_pb2'
  # @@protoc_insertion_point(class_scope:protos.ProtoMetadata)
  ))
_sym_db.RegisterMessage(ProtoMetadata)

ProtoTags = _reflection.GeneratedProtocolMessageType('ProtoTags', (_message.Message,), dict(
  DESCRIPTOR = _PROTOTAGS,
  __module__ = 'featureMessages_pb2'
  # @@protoc_insertion_point(class_scope:protos.ProtoTags)
  ))
_sym_db.RegisterMessage(ProtoTags)

ProtoTag = _reflection.GeneratedProtocolMessageType('ProtoTag', (_message.Message,), dict(
  DESCRIPTOR = _PROTOTAG,
  __module__ = 'featureMessages_pb2'
  # @@protoc_insertion_point(class_scope:protos.ProtoTag)
  ))
_sym_db.RegisterMessage(ProtoTag)

ProtoFeatureCellValue = _reflection.GeneratedProtocolMessageType('ProtoFeatureCellValue', (_message.Message,), dict(
  DESCRIPTOR = _PROTOFEATURECELLVALUE,
  __module__ = 'featureMessages_pb2'
  # @@protoc_insertion_point(class_scope:protos.ProtoFeatureCellValue)
  ))
_sym_db.RegisterMessage(ProtoFeatureCellValue)

ProtoCellValue = _reflection.GeneratedProtocolMessageType('ProtoCellValue', (_message.Message,), dict(
  DESCRIPTOR = _PROTOCELLVALUE,
  __module__ = 'featureMessages_pb2'
  # @@protoc_insertion_point(class_scope:protos.ProtoCellValue)
  ))
_sym_db.RegisterMessage(ProtoCellValue)


# @@protoc_insertion_point(module_scope)
