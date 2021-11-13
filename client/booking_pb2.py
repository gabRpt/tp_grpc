# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: booking.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='booking.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rbooking.proto\"\x0e\n\x0c\x45mptyMessage\"Y\n\x04\x42ook\x12\x0e\n\x06userid\x18\x01 \x01(\t\x12\x1a\n\x05\x64\x61tes\x18\x02 \x03(\x0b\x32\x0b.Book.Dates\x1a%\n\x05\x44\x61tes\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x0e\n\x06movies\x18\x02 \x03(\t\"\x18\n\x06UserId\x12\x0e\n\x06userid\x18\x01 \x01(\t\":\n\x0bReservation\x12\x0e\n\x06userid\x18\x01 \x01(\t\x12\r\n\x05movie\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x03 \x01(\t\"8\n\x17\x41\x64\x64\x42ookingReturnMessage\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t2\x97\x01\n\x07\x42ooking\x12)\n\x0fGetListBookings\x12\r.EmptyMessage\x1a\x05.Book0\x01\x12+\n\x17GetListBookingsFromUser\x12\x07.UserId\x1a\x05.Book0\x01\x12\x34\n\nAddBooking\x12\x0c.Reservation\x1a\x18.AddBookingReturnMessageb\x06proto3'
)




_EMPTYMESSAGE = _descriptor.Descriptor(
  name='EmptyMessage',
  full_name='EmptyMessage',
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
  serialized_start=17,
  serialized_end=31,
)


_BOOK_DATES = _descriptor.Descriptor(
  name='Dates',
  full_name='Book.Dates',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='date', full_name='Book.Dates.date', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='movies', full_name='Book.Dates.movies', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=85,
  serialized_end=122,
)

_BOOK = _descriptor.Descriptor(
  name='Book',
  full_name='Book',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userid', full_name='Book.userid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dates', full_name='Book.dates', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_BOOK_DATES, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=122,
)


_USERID = _descriptor.Descriptor(
  name='UserId',
  full_name='UserId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userid', full_name='UserId.userid', index=0,
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
  serialized_start=124,
  serialized_end=148,
)


_RESERVATION = _descriptor.Descriptor(
  name='Reservation',
  full_name='Reservation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userid', full_name='Reservation.userid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='movie', full_name='Reservation.movie', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='date', full_name='Reservation.date', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=150,
  serialized_end=208,
)


_ADDBOOKINGRETURNMESSAGE = _descriptor.Descriptor(
  name='AddBookingReturnMessage',
  full_name='AddBookingReturnMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='AddBookingReturnMessage.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='AddBookingReturnMessage.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=210,
  serialized_end=266,
)

_BOOK_DATES.containing_type = _BOOK
_BOOK.fields_by_name['dates'].message_type = _BOOK_DATES
DESCRIPTOR.message_types_by_name['EmptyMessage'] = _EMPTYMESSAGE
DESCRIPTOR.message_types_by_name['Book'] = _BOOK
DESCRIPTOR.message_types_by_name['UserId'] = _USERID
DESCRIPTOR.message_types_by_name['Reservation'] = _RESERVATION
DESCRIPTOR.message_types_by_name['AddBookingReturnMessage'] = _ADDBOOKINGRETURNMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EmptyMessage = _reflection.GeneratedProtocolMessageType('EmptyMessage', (_message.Message,), {
  'DESCRIPTOR' : _EMPTYMESSAGE,
  '__module__' : 'booking_pb2'
  # @@protoc_insertion_point(class_scope:EmptyMessage)
  })
_sym_db.RegisterMessage(EmptyMessage)

Book = _reflection.GeneratedProtocolMessageType('Book', (_message.Message,), {

  'Dates' : _reflection.GeneratedProtocolMessageType('Dates', (_message.Message,), {
    'DESCRIPTOR' : _BOOK_DATES,
    '__module__' : 'booking_pb2'
    # @@protoc_insertion_point(class_scope:Book.Dates)
    })
  ,
  'DESCRIPTOR' : _BOOK,
  '__module__' : 'booking_pb2'
  # @@protoc_insertion_point(class_scope:Book)
  })
_sym_db.RegisterMessage(Book)
_sym_db.RegisterMessage(Book.Dates)

UserId = _reflection.GeneratedProtocolMessageType('UserId', (_message.Message,), {
  'DESCRIPTOR' : _USERID,
  '__module__' : 'booking_pb2'
  # @@protoc_insertion_point(class_scope:UserId)
  })
_sym_db.RegisterMessage(UserId)

Reservation = _reflection.GeneratedProtocolMessageType('Reservation', (_message.Message,), {
  'DESCRIPTOR' : _RESERVATION,
  '__module__' : 'booking_pb2'
  # @@protoc_insertion_point(class_scope:Reservation)
  })
_sym_db.RegisterMessage(Reservation)

AddBookingReturnMessage = _reflection.GeneratedProtocolMessageType('AddBookingReturnMessage', (_message.Message,), {
  'DESCRIPTOR' : _ADDBOOKINGRETURNMESSAGE,
  '__module__' : 'booking_pb2'
  # @@protoc_insertion_point(class_scope:AddBookingReturnMessage)
  })
_sym_db.RegisterMessage(AddBookingReturnMessage)



_BOOKING = _descriptor.ServiceDescriptor(
  name='Booking',
  full_name='Booking',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=269,
  serialized_end=420,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetListBookings',
    full_name='Booking.GetListBookings',
    index=0,
    containing_service=None,
    input_type=_EMPTYMESSAGE,
    output_type=_BOOK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetListBookingsFromUser',
    full_name='Booking.GetListBookingsFromUser',
    index=1,
    containing_service=None,
    input_type=_USERID,
    output_type=_BOOK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AddBooking',
    full_name='Booking.AddBooking',
    index=2,
    containing_service=None,
    input_type=_RESERVATION,
    output_type=_ADDBOOKINGRETURNMESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_BOOKING)

DESCRIPTOR.services_by_name['Booking'] = _BOOKING

# @@protoc_insertion_point(module_scope)
