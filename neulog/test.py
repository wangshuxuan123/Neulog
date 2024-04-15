# --coding:utf-8--
import ctypes
import time
import datetime
from ctypes import *

lib = ctypes.cdll.LoadLibrary("D:/C_project/neulog_test/x64/Debug/neulog_test.dll")

#dllObj = CDLL("D:/C_project/neulog_test/x64/Debug/neulog_test.dll")
lib.getSensorTime.restype = c_char_p
port = bytes("COM9", "utf-8")
stype = chr(36).encode("utf-8")
sid = chr(1).encode("utf-8")
# lib.neulog_read(port)


if lib.sensor_init(port):
    # sensor_time = lib.getSensorTime().decode()
    # print('0:', sensor_time)

    while (True):
        # lib.sendGetCmd(stype+sid)
        print('1',datetime.datetime.now())
        time.sleep(0.001)
        print('2',datetime.datetime.now())
        sensor_data = lib.getSensorData(stype+sid)
        print('3', datetime.datetime.now())
        #print(sensor_data)
        #print(datetime.datetime.now(), sensor_data)
        # sensor_time = lib.getSensorTime().decode()
        # print('2:',sensor_time)


