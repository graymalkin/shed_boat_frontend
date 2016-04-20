#! /usr/bin/python

import boat_pb2
import serial
import sys
import time
def validateReceivedPacket(potentialPacket):
    bytesIn = bytearray()
    bytesIn.extend(potentialPacket)

    length = bytesIn[2]
    data_start = 14
    data = bytesIn[data_start:-1]
    calced_check = 0xff - (int(sum(bytesIn[2:-1])) & 0xff)
    checksum = bytesIn[-1]
    if calced_check != checksum:
        print "Invalid checksum (0x{:02x}), expected 0x{:02x}".format(checksum, calced_check)
        return None

    frameType = hex(bytesIn[2])

    # print "Length: {:d}".format(length)
    # print "Data Start: {:d}".format(data_start)
    # print " ".join(["{:02x}".format(x) for x in data])

    return data

def status_to_string(status):
	return ["UNDEFINED", "UNDERWAY_MANUAL", "UNDERWAY_AUTOPILOT", "STATIONARY", "RESTRICTED_MANEUVERABILITY"][status]
def quality_to_string(quality):
	return ["IDEAL", "EXCELLENT", "GOOD", "MODERATE", "FAIR", "SHIT"][quality]

#  Try outputting the message.
def ListTelemetry(telemetry):
    print "Boat Status:", status_to_string(telemetry.status)
    if telemetry.HasField('location'):
            if telemetry.location.HasField('latitude'):
                print "Latitude:", telemetry.location.latitude
            if telemetry.location.HasField('longitude'):
                print "Longitude:", telemetry.location.longitude
            if telemetry.location.HasField('number_of_satellites_visible'):
                print "Satellites Visible:", telemetry.location.number_of_satellites_visible
            if telemetry.location.HasField('speed_over_ground'):
                print "Speed Over Ground:", telemetry.location.speed_over_ground
            if telemetry.location.HasField('true_heading'):
                print "True Heading:", float(telemetry.location.true_heading / 1000)
            if telemetry.location.HasField('true_bearing'):
                print "True Bearing:", float(telemetry.location.true_bearing / 1000)
            if telemetry.location.HasField('utc_seconds'):
                print "UTC Seconds:", telemetry.location.utc_seconds
            if telemetry.location.HasField('fix_quality'):
				print "Fix Quality:", quality_to_string(telemetry.location.fix_quality)
    for motor in telemetry.motor:
        print "Motor Number", motor.motor_number
        if motor.HasField('is_alive'):
            print "Motor %d Is Alive?: %s" % (motor.motor_number, motor.is_alive,)
        if motor.HasField('rpm'):
            print "Motor %d Rpm: %s" % (motor.motor_number, motor.rpm,)
        if motor.HasField('temperature'):
            print "Motor %d Temperature: %s" % (motor.motor_number, motor.temperature,)
        if motor.HasField('voltage'):
            print "Motor %d Voltage: %s" % (motor.motor_number, motor.voltage,)
        if motor.HasField('voltage'):
            print "Motor %d Current: %s" % (motor.motor_number, motor.current,)
    if telemetry.HasField('debug'):
            if telemetry.debug.HasField('bearing_compensation'):
                print "Bearing Compensation:", float(telemetry.debug.bearing_compensation /1000)
            if telemetry.debug.HasField('speed_over_ground_compensation'):
                print "Speed Compensation:", float(telemetry.debug.speed_over_ground_compensation /1000)
            if telemetry.debug.HasField('motor_1_throttle_compensation'):
                print "Motor 1 Throttle Compensation:", float(telemetry.debug.motor_1_throttle_compensation / 1000)
            if telemetry.debug.HasField('motor_2_throttle_compensation'):
                print "Motor 2 Throttle Compensation:", float(telemetry.debug.motor_2_throttle_compensation / 1000)
    print ""
    sys.stdout.flush()
try:
    with serial.Serial('COM4', 115200) as ser:
        rxBuffer = bytearray()
        while True:
            tdata = rxBuffer;
            tdata.append(ser.read()) # Block until we receive data
            time.sleep(1) # Let data pool in serial input buffer
            remaining = ser.inWaiting() # Read in the rest of data in buffer
            tdata.extend(ser.read(remaining))
            ser.flushInput() # Clear the serial input buffer

            # If we've collected more than on packet
            # Splits the potential multiple packets recieved
            packets = tdata[1:].split(bytes(b'\x7E'))

            rxBuffer = bytearray() # Clear the rxBuffer and prepare for any malformed packets

            for potentialPacket in packets:
                payload = validateReceivedPacket(potentialPacket)
                if (payload is not None):
                    telemetry = boat_pb2.Telemetry()
                    telemetry.ParseFromString(str(payload))
                    ListTelemetry(telemetry)

#print "\r\n"
except KeyboardInterrupt:
    print "Exiting read thread..."
