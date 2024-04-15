# --coding:utf-8--
import thread
from Queue import Queue
from collections import deque
import numpy as np
import socket
import time
from neulog import gsr
import threading
"""
Sample GSR experiment.

Gathers data over two phases. Use a keyboard interrupt (control-c) to end a phase.

Saves data to disk afterwards.
"""

class sensor_start(threading.Thread):
    def __init__(self, sensor, stype, sid):
        threading.Thread.__init__(self)
        #self.sensor = gsr()
        self.sensor = sensor
        self.stype = stype
        self.sid = sid
        self.x = 0.
        self.data = [0. for _ in range(100)]
        self.buffer = []
        self.times = []
        self.t0 = time.time()
        self.start()
    def run(self):

        print("Start Sensor...")
        while True:  # first phase (eg. 'resting')
            try:
                self.x = self.sensor.get_data(self.stype, self.sid)

                t = time.time() - self.t0
                print t, self.x
                self.times.append(t)
                self.data.append([t, self.x])
                #print(self.data[-1])
            except KeyboardInterrupt:
                break


    def tcp_send(self):
        while True:

            time.sleep(0.05)
            print self.data[-1]

# tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# #sever_ip = "192.168.33.100"
# sever_ip = "0.0.0.0"
# sever_port = 8000
# # 设置端口复用
# tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
# tcp_server_socket.bind(("", 8000))
# # 监听
# tcp_server_socket.listen(128)
# # 等待客户建立连接
# tcp_client, tcp_client_address = tcp_server_socket.accept()
#
# #接受数据
#
# recv_data= tcp_client.recv(1024)
#
# print"客户端发送的数据为:",recv_data
#
# # 发送数据
# n = 0
# while n < 100:
#     time.sleep(0.1)
#     tcp_client.send('244'.encode())
# tcp_client.close()

if __name__ == "__main__":
    sensor = gsr()
    thread1 = sensor_start(sensor, 36, 1)
    thread2 = sensor_start(sensor, 8, 2)
    # thread.start_new_thread(ss.run1, (36, 1))
    #thread.start_new_thread(ss.run2, (8, 2))
    # time.sleep(0.5)
    # thread2 = thread.start_new_thread(thread1.tcp_send,())

