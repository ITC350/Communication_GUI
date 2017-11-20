from bt import Bluetooth

class Protocol(object):
    execute = 0x00
    forward = 0x01
    backward = 0x02
    turn = 0x03
    brake = 0x04
    halt = 0xFF

    def __init__(self, mac_addr, config = []):
        self.bluetooth = Bluetooth(mac_addr, 1)
        self.config = config

    def __enter__(self):
        self.bluetooth.open()
    
    def __exit__(self, exception_type, exception_value, traceback):
        self.bluetooth.close()

    def halt(self):
        self.config.send_msg(self.halt)

    def execute(self):
        self.config.append(self.execute)
        self.bluetooth.send_msg(self.config)

    def forward(self, seconds = 1):
        self.config.append(self.forward)
        self.config.append(seconds)
    
    def backward(self, seconds = 1):
        self.config.append(self.backward)
        self.config.append(seconds)
    
    def turn(self, angle):
        self.config.append(self.turn)
        self.config.append(angle)
    
    def brake(self):
        self.config.append(self.brake)