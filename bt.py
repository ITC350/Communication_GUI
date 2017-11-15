import bluetooth

max_data_size = 128

def open_bt(mac_addr, port):
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((mac_addr, port))
    return sock

def close_bt(bt):
    bt.close()

def send_msg(bt, msg):
    bt.send(msg)

def receive_msg(bt, msg, size = max_data_size):
    return bt.recv(size)

sock = open_bt('98:D3:32:20:82:CA', 1)
data = sock.recv(2)

print(data)
