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

#  Try outputting the message.
def ListTelemetry(telemetry):
    print "Boat Status:", telemetry.status
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
                print "True Heading:", telemetry.location.true_heading
            if telemetry.location.HasField('true_bearing'):
                print "True Bearing:", telemetry.location.true_bearing
            if telemetry.location.HasField('utc_seconds'):
                print "UTC Seconds:", telemetry.location.utc_seconds
            for x in range(0, 2):
                print "Motor Number", telemetry.motor[x].motor_number
                if telemetry.motor[x].HasField('is_alive'):
                    print "Motor %d Is Alive?: %s" % (x, telemetry.motor[x].is_alive,)
                if telemetry.motor[x].HasField('rpm'):
                    print "Motor %d Rpm: %s" % (x, telemetry.motor[x].rpm,)
                if telemetry.motor[x].HasField('temperature'):
                    print "Motor %d Temperature: %s" % (x, telemetry.motor[x].temperature,)
                if telemetry.motor[x].HasField('voltage'):
                    print "Motor %d Voltage: %s" % (x, telemetry.motor[x].voltage,)
                if telemetry.motor[x].HasField('voltage'):
                    print "Motor %d Current: %s" % (x, telemetry.motor[x].current,)
            if telemetry.HasField('debug'):
                if telemetry.debug.HasField('bearing_compensation'):
                    print "Bearing Compensation:", telemetry.debug.bearing_compensation
                if telemetry.debug.HasField('speed_over_ground_compensation'):
                    print "Speed Compensation:", telemetry.debug.speed_over_ground_compensation
                if telemetry.debug.HasField('tmotor_1_throttle_compensation'):
                    print "Motor 1 Throttle Compensation:", telemetry.debug.motor_1_throttle_compensation
                if telemetry.debug.HasField('motor_2_throttle_compensation'):
                    print "Motor 2 Throttle Compensation:", telemetry.debug.motor_2_throttle_compensation
            print ""
try:
    with serial.Serial('/dev/tty.usbserial-A6009s3y', 9600) as ser:
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
