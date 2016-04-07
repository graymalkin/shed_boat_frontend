# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: examples/boat.proto

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
  name='examples/boat.proto',
  package='shedBoat',
  serialized_pb=_b('\n\x13\x65xamples/boat.proto\x12\x08shedBoat\"\xc2\x02\n\tTelemetry\x12\x35\n\x06status\x18\x01 \x02(\x0e\x32\x1a.shedBoat.Telemetry.Status:\tUNDEFINED\x12$\n\x08location\x18\x02 \x01(\x0b\x32\x12.shedBoat.Location\x12\x1e\n\x05motor\x18\x03 \x03(\x0b\x32\x0f.shedBoat.Motor\x12\"\n\x07\x62\x61ttery\x18\x04 \x01(\x0b\x32\x11.shedBoat.Battery\x12\x1e\n\x05\x64\x65\x62ug\x18\x05 \x01(\x0b\x32\x0f.shedBoat.Debug\"t\n\x06Status\x12\r\n\tUNDEFINED\x10\x00\x12\x13\n\x0fUNDERWAY_MANUAL\x10\x01\x12\x16\n\x12UNDERWAY_AUTOPILOT\x10\x02\x12\x0e\n\nSTATIONARY\x10\x03\x12\x1e\n\x1aRESTRICTED_MANEUVERABILITY\x10\x04\"\xb1\x01\n\x08Location\x12\x10\n\x08latitude\x18\x01 \x01(\x02\x12\x11\n\tlongitude\x18\x02 \x01(\x02\x12$\n\x1cnumber_of_satellites_visible\x18\x03 \x01(\x05\x12\x19\n\x11speed_over_ground\x18\x04 \x01(\x02\x12\x14\n\x0ctrue_heading\x18\x05 \x01(\x02\x12\x14\n\x0ctrue_bearing\x18\x06 \x01(\x01\x12\x13\n\x0butc_seconds\x18\x07 \x01(\x05\"s\n\x05Motor\x12\x14\n\x0cmotor_number\x18\x01 \x02(\x05\x12\x10\n\x08is_alive\x18\x02 \x01(\x08\x12\x0b\n\x03rpm\x18\x03 \x01(\x05\x12\x13\n\x0btemperature\x18\x04 \x01(\x05\x12\x0f\n\x07voltage\x18\x05 \x01(\x05\x12\x0f\n\x07\x63urrent\x18\x06 \x01(\x05\"s\n\x07\x42\x61ttery\x12\x14\n\x0cpercent_full\x18\x01 \x01(\x05\x12$\n\x04\x63\x65ll\x18\x02 \x03(\x0b\x32\x16.shedBoat.Battery.Cell\x1a,\n\x04\x43\x65ll\x12\x13\n\x0b\x63\x65ll_number\x18\x01 \x02(\x05\x12\x0f\n\x07voltage\x18\x02 \x01(\x05\"\x9b\x01\n\x05\x44\x65\x62ug\x12\x1c\n\x14\x62\x65\x61ring_compensation\x18\x01 \x01(\x02\x12&\n\x1espeed_over_ground_compensation\x18\x02 \x01(\x02\x12%\n\x1dmotor_1_throttle_compensation\x18\x03 \x01(\x02\x12%\n\x1dmotor_2_throttle_compensation\x18\x04 \x01(\x02')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_TELEMETRY_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='shedBoat.Telemetry.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNDERWAY_MANUAL', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNDERWAY_AUTOPILOT', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATIONARY', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESTRICTED_MANEUVERABILITY', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=240,
  serialized_end=356,
)
_sym_db.RegisterEnumDescriptor(_TELEMETRY_STATUS)


_TELEMETRY = _descriptor.Descriptor(
  name='Telemetry',
  full_name='shedBoat.Telemetry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='shedBoat.Telemetry.status', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='location', full_name='shedBoat.Telemetry.location', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='motor', full_name='shedBoat.Telemetry.motor', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battery', full_name='shedBoat.Telemetry.battery', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='debug', full_name='shedBoat.Telemetry.debug', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TELEMETRY_STATUS,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=34,
  serialized_end=356,
)


_LOCATION = _descriptor.Descriptor(
  name='Location',
  full_name='shedBoat.Location',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='latitude', full_name='shedBoat.Location.latitude', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='shedBoat.Location.longitude', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='number_of_satellites_visible', full_name='shedBoat.Location.number_of_satellites_visible', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='speed_over_ground', full_name='shedBoat.Location.speed_over_ground', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='true_heading', full_name='shedBoat.Location.true_heading', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='true_bearing', full_name='shedBoat.Location.true_bearing', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='utc_seconds', full_name='shedBoat.Location.utc_seconds', index=6,
      number=7, type=5, cpp_type=1, label=1,
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
  serialized_start=359,
  serialized_end=536,
)


_MOTOR = _descriptor.Descriptor(
  name='Motor',
  full_name='shedBoat.Motor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='motor_number', full_name='shedBoat.Motor.motor_number', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_alive', full_name='shedBoat.Motor.is_alive', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rpm', full_name='shedBoat.Motor.rpm', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='temperature', full_name='shedBoat.Motor.temperature', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='voltage', full_name='shedBoat.Motor.voltage', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='current', full_name='shedBoat.Motor.current', index=5,
      number=6, type=5, cpp_type=1, label=1,
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
  serialized_start=538,
  serialized_end=653,
)


_BATTERY_CELL = _descriptor.Descriptor(
  name='Cell',
  full_name='shedBoat.Battery.Cell',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cell_number', full_name='shedBoat.Battery.Cell.cell_number', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='voltage', full_name='shedBoat.Battery.Cell.voltage', index=1,
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
  oneofs=[
  ],
  serialized_start=726,
  serialized_end=770,
)

_BATTERY = _descriptor.Descriptor(
  name='Battery',
  full_name='shedBoat.Battery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='percent_full', full_name='shedBoat.Battery.percent_full', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cell', full_name='shedBoat.Battery.cell', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_BATTERY_CELL, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=655,
  serialized_end=770,
)


_DEBUG = _descriptor.Descriptor(
  name='Debug',
  full_name='shedBoat.Debug',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bearing_compensation', full_name='shedBoat.Debug.bearing_compensation', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='speed_over_ground_compensation', full_name='shedBoat.Debug.speed_over_ground_compensation', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='motor_1_throttle_compensation', full_name='shedBoat.Debug.motor_1_throttle_compensation', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='motor_2_throttle_compensation', full_name='shedBoat.Debug.motor_2_throttle_compensation', index=3,
      number=4, type=2, cpp_type=6, label=1,
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
  serialized_start=773,
  serialized_end=928,
)

_TELEMETRY.fields_by_name['status'].enum_type = _TELEMETRY_STATUS
_TELEMETRY.fields_by_name['location'].message_type = _LOCATION
_TELEMETRY.fields_by_name['motor'].message_type = _MOTOR
_TELEMETRY.fields_by_name['battery'].message_type = _BATTERY
_TELEMETRY.fields_by_name['debug'].message_type = _DEBUG
_TELEMETRY_STATUS.containing_type = _TELEMETRY
_BATTERY_CELL.containing_type = _BATTERY
_BATTERY.fields_by_name['cell'].message_type = _BATTERY_CELL
DESCRIPTOR.message_types_by_name['Telemetry'] = _TELEMETRY
DESCRIPTOR.message_types_by_name['Location'] = _LOCATION
DESCRIPTOR.message_types_by_name['Motor'] = _MOTOR
DESCRIPTOR.message_types_by_name['Battery'] = _BATTERY
DESCRIPTOR.message_types_by_name['Debug'] = _DEBUG

Telemetry = _reflection.GeneratedProtocolMessageType('Telemetry', (_message.Message,), dict(
  DESCRIPTOR = _TELEMETRY,
  __module__ = 'examples.boat_pb2'
  # @@protoc_insertion_point(class_scope:shedBoat.Telemetry)
  ))
_sym_db.RegisterMessage(Telemetry)

Location = _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), dict(
  DESCRIPTOR = _LOCATION,
  __module__ = 'examples.boat_pb2'
  # @@protoc_insertion_point(class_scope:shedBoat.Location)
  ))
_sym_db.RegisterMessage(Location)

Motor = _reflection.GeneratedProtocolMessageType('Motor', (_message.Message,), dict(
  DESCRIPTOR = _MOTOR,
  __module__ = 'examples.boat_pb2'
  # @@protoc_insertion_point(class_scope:shedBoat.Motor)
  ))
_sym_db.RegisterMessage(Motor)

Battery = _reflection.GeneratedProtocolMessageType('Battery', (_message.Message,), dict(

  Cell = _reflection.GeneratedProtocolMessageType('Cell', (_message.Message,), dict(
    DESCRIPTOR = _BATTERY_CELL,
    __module__ = 'examples.boat_pb2'
    # @@protoc_insertion_point(class_scope:shedBoat.Battery.Cell)
    ))
  ,
  DESCRIPTOR = _BATTERY,
  __module__ = 'examples.boat_pb2'
  # @@protoc_insertion_point(class_scope:shedBoat.Battery)
  ))
_sym_db.RegisterMessage(Battery)
_sym_db.RegisterMessage(Battery.Cell)

Debug = _reflection.GeneratedProtocolMessageType('Debug', (_message.Message,), dict(
  DESCRIPTOR = _DEBUG,
  __module__ = 'examples.boat_pb2'
  # @@protoc_insertion_point(class_scope:shedBoat.Debug)
  ))
_sym_db.RegisterMessage(Debug)


# @@protoc_insertion_point(module_scope)
