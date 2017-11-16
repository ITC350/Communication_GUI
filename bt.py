import bluetooth
from config import default_msg_size, mac_addr, port

class Bluetooth:
    def __init__(self, mac_addr, port = 1, default_msg_size = 128):
        self.sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self.mac_addr = mac_addr
        self.port = port
        self.default_msg_size = default_msg_size
    
    def open(self):
        self.sock.connect((mac_addr, port))

    def close_bt(self, sock):
        self.sock.close()

    def send_msg(self, msg):
        self.sock.send(msg)

    def receive_msg(self, msg, size = default_msg_size):
        return self.sock.recv(size)


