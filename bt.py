from bluetooth import BluetoothSocket, RFCOMM

class Bluetooth(BluetoothSocket):
    def __init__(self, mac_addr, port = 1):
        super(Bluetooth, self).__init__(RFCOMM)
        self.mac_addr = mac_addr
        self.port = port
    
    def open(self):
        self.connect((self.mac_addr, self.port))

    def close(self):
        self.close()

    def send_msg(self, msg):
        self.send(msg)

    def receive_msg(self, msg, size = 32):
        return self.recv(size)