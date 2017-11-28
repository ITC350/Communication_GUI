from bt import Bluetooth
import array

bt_dev = Bluetooth('98:D3:32:20:82:CA')
bt_dev.open()

start = 0x01
settings = 0x02

s = bytearray(struct.pack("b", settings)) + 
bytearray(struct.pack("i", 2)) +
bytearray(struct.pack("i", 0)) +
bytearray(struct.pack("i", 0)) +
bytearray(struct.pack("i", 500)) + 
bytearray(struct.pack("i", 50)) +
bytearray(struct.pack("i", 50)) +
bytearray(struct.pack("b", start))

bt_dev.send_msg(bytearray(struct.pack('b', 0)))
#bt_dev.send_msg(s)
msg = bt_dev.receive_msg(2048)
msg = array.array('H', msg)
print(msg.tostring())
