from bt import Bluetooth
import struct
import array

api = {
    'nop' : 0x00,
    'start' : 0x01,
    'settings' : 0x02,
    'disable_abs' : 0x03,
    'halt' : 0x04
}

class Protocol(object):
    def __init__(self, mac_addr, msg_size):
        self.bluetooth = Bluetooth(mac_addr, 1)
        self.config = b''
        self.msg_size = msg_size
    
    def __enter__(self):
        self.bluetooth.open()
    
    def __exit__(self, exception_type, exception_value, traceback):
        self.bluetooth.close()

    def send(self):
        self.bluetooth.send_msg(config)

    def receive(self, size = 127):
        self.bluetooth.receive(size)

    def halt(self):
        self.bluetooth.send_msg(struct.pack('b', api['halt']))

    def disable_abs(self):
        self.config += struct.pack('b', api['disable_abs'])

    def start(self):
        self.config += struct.pack('b', api['start'])
        for i in range(0, self.msg_size - len(self.config)):
            self.nop()

    def settings(self, args):
        self.config += struct.pack('b', api['settings'])
        for a in args:
            self.config += struct.pack('I', a)

    def nop(self):
        self.config += struct.pack('b', api['nop'])
