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

# Read the existing address book.
with serial.Serial('/dev/tty.usbmodem1422', 115200) as ser:
    len = ser.read()
    message = ser.read(len)
    telemetry.ParseFromString(message)
    ListTelemetry(telemetry)
