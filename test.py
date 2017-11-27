from bt import Bluetooth

bt_dev = Bluetooth('98:D3:32:20:82:CA')

while True:
    msg = input("msg to send")
    bt_dev.send_msg(msg)
