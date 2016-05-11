# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ratings.proto

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
  name='ratings.proto',
  package='org.convox.board',
  serialized_pb=_b('\n\rratings.proto\x12\x10org.convox.board\"\x8d\x01\n\x0bUserRatings\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12>\n\x0cgame_ratings\x18\x02 \x03(\x0b\x32(.org.convox.board.UserRatings.GameRating\x1a-\n\nGameRating\x12\x0f\n\x07game_id\x18\x01 \x01(\t\x12\x0e\n\x06rating\x18\x02 \x01(\r')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_USERRATINGS_GAMERATING = _descriptor.Descriptor(
  name='GameRating',
  full_name='org.convox.board.UserRatings.GameRating',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='game_id', full_name='org.convox.board.UserRatings.GameRating.game_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rating', full_name='org.convox.board.UserRatings.GameRating.rating', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  oneofs=[
  ],
  serialized_start=132,
  serialized_end=177,
)

_USERRATINGS = _descriptor.Descriptor(
  name='UserRatings',
  full_name='org.convox.board.UserRatings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='org.convox.board.UserRatings.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='game_ratings', full_name='org.convox.board.UserRatings.game_ratings', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_USERRATINGS_GAMERATING, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=36,
  serialized_end=177,
)

_USERRATINGS_GAMERATING.containing_type = _USERRATINGS
_USERRATINGS.fields_by_name['game_ratings'].message_type = _USERRATINGS_GAMERATING
DESCRIPTOR.message_types_by_name['UserRatings'] = _USERRATINGS

UserRatings = _reflection.GeneratedProtocolMessageType('UserRatings', (_message.Message,), dict(

  GameRating = _reflection.GeneratedProtocolMessageType('GameRating', (_message.Message,), dict(
    DESCRIPTOR = _USERRATINGS_GAMERATING,
    __module__ = 'ratings_pb2'
    # @@protoc_insertion_point(class_scope:org.convox.board.UserRatings.GameRating)
    ))
  ,
  DESCRIPTOR = _USERRATINGS,
  __module__ = 'ratings_pb2'
  # @@protoc_insertion_point(class_scope:org.convox.board.UserRatings)
  ))
_sym_db.RegisterMessage(UserRatings)
_sym_db.RegisterMessage(UserRatings.GameRating)


# @@protoc_insertion_point(module_scope)