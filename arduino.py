# --coding:utf-8--
import time

import serial

STX = chr(85)
IN_READ = chr(49)
class arduino_serial(serial.Serial):
    def __init__(self, port='COM10'):
        serial.Serial.__init__(
            self,
            port=port,
            baudrate=115200,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_TWO,
            bytesize=serial.EIGHTBITS,
            timeout=1
        )

    def send(self):
        cmd = STX + chr(36) + chr(1) + IN_READ + (3 * chr(0))
        while True:
            time.sleep(0.5)
            self.flushInput()
            self.flushOutput()
            self.write(cmd.encode())
            # self.write(cmd)

            time.sleep(0.1)
            print(self.read(50))
            # self.write(chr(171).encode())
            # self.write(chr(171))
            self.write(bytes.fromhex('ab'))
            print(self.read(50))
if __name__ == '__main__':
    ad = arduino_serial()
    ad.send()

