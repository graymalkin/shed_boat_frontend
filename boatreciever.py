#! /usr/bin/python

import boat_pb2
import serial
import sys

# Iterates though all telemetry messages and prints a subset of location.
def ListTelemetry(telemetry):
    if telemetry.HasField('location'):
            print "latitude:", telemetry.location.latitude
            print "longitude:", telemetry.location.longitude

# Main procedure:  Reads the entire address book from a file and prints all
#   the information inside.
telemetry = boat_pb2.Telemetry()

try:
    with serial.Serial('/dev/tty.usbserial-A6009s3y', 115200) as ser:
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

            #print "Packets found:",len(packets)

            rxBuffer = bytearray() # Clear the rxBuffer and prepare for any malformed packets

            for potentialPacket in packets:
                payload = validateReceivedPacket(potentialPacket)
                if (payload is not NONE):
                    telemetry.ParseFromString(payload)
                    ListTelemetry(telemetry)
        #print "\r\n"
except KeyboardInterrupt:
    print "Exiting read thread..."


def validateReceivedPacket(potentialPacket):
    bytesIn = bytearray()
    bytesIn.extend(potentialPacket)

    # Checks whether the frame is of the minimum size needed
    # 9 bytes is the minimum length of a rx frame without a payload
    # This removes the need to check against escaped characters also
    if (len(bytesIn) - bytesIn.count(bytes(b'0x07D')) < 9):
        return None

    length = bytesIn[1]

    # Does the packet match the length it claims?
    # Especially useful to detect when we've only got 'half' a packet
    if length > (len(bytesIn[2:])-1):
        return None

    checksum = hex(bytesIn[len(bytesIn)-1])
    frameType = hex(bytesIn[2])

    # Checksum check
    if (sum(bytesIn[2:3+length]) & 0xFF) != 0xFF:
    	return None


    payload = bytearray()
    payload.extend(packet[15:len(packet)-2])

    return payload
