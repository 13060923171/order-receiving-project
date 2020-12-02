#!/usr/bin/python
# coding=UTF-8
import serial
from flask_sqlalchemy import xrange


def hexshow(data):
    hex_data = ''
    hLen = len(data)
    for i in xrange(hLen):
        hvol = ord(data[i])
        hhex = '%02x' % hvol
        hex_data += hhex+' '
        print('hexshow:', hex_data)

def hexsend(string_data=''):
    hex_data = string_data.decode("hex")
    return hex_data

if __name__ == '__main__':
    serial = serial.Serial('COM4', 115200)
    print(serial)
    if serial.isOpen():
        print("open success")
    else:
        print("open failed")
    try:
        while True:
            count = serial.inWaiting()
            if count > 0:
                data = serial.read(count)
                if data != b'':
                    print("receive:", data)
                    serial.write(data)
                else:
                    serial.write(hexsend(data))
    except KeyboardInterrupt:
        if serial != None:
            serial.close()