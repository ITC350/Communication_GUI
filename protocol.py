from bt import Bluetooth

cmds = {
    'execute' : 0x00,
    'forward' : 0x01,
    'backward' : 0x02,
    'turn' : 0x03,
    'brake' : 0x04,
    'halt' : 0xFF
}

class Protocol(object):
    def __init__(self, mac_addr, cmds, config = []):
        self.bluetooth = Bluetooth(mac_addr, 1)
        self.config = config
        self.api = cmds

    def __enter__(self):
        self.bluetooth.open()
    
    def __exit__(self, exception_type, exception_value, traceback):
        self.bluetooth.close()

    def halt(self):
        self.config.send_msg(self.api['halt'])

    def execute(self):
        self.config.append(self.api['execute'])
        self.bluetooth.send_msg(self.config)

    def forward(self, seconds = 1):
        self.config.append(self.api['forward'])
        self.config.append(seconds)
    
    def backward(self, seconds = 1):
        self.config.append(self.api['backward'])
        self.config.append(seconds)
    
    def turn(self, angle):
        self.config.append(self.api['turn'])
        self.config.append(angle)
    
    def brake(self):
        self.config.append(self.api['brake'])

    def build(self, cmds):
        for c in cmds:
            if c in self.api.keys:
                self.config.append(c)
            else:
                self.config = []
                return "Invalid command: " + c
