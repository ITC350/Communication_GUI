from bt import Bluetooth
import array
import struct

bt_dev = Bluetooth('98:D3:32:20:82:CA')
bt_dev.open()

start = 0x01
settings = 0x02

s = bytearray(struct.pack("b", settings)) + bytearray(struct.pack("I", 2)) + bytearray(struct.pack("I", 0)) + bytearray(struct.pack("I", 0)) + bytearray(struct.pack("I", 500)) + bytearray(struct.pack("I", 50)) + bytearray(struct.pack("I", 50)) + bytearray(struct.pack("b", start)) + bytearray(struct.pack("Q", 0))
print(bytes(s))

bt_dev.send_msg(bytes(s))

msg = b''

for i in range(0, 16):
    msg = msg + bt_dev.receive_msg(127)

msg = msg + bt_dev.receive_msg(16)

print(str(msg))
#msg = array.array('H', msg)
#print(msg.tostring())
