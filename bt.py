import bluetooth
from config import default_msg_size, mac_addr, port

def open_bt(mac_addr, port):
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((mac_addr, port))
    return sock

def close_bt(sock):
    sock.close()

def send_msg(sock, msg):
    sock.send(msg)

def receive_msg(sock, msg, size = default_msg_size):
    return sock.recv(size)

#sock = open_bt(mac_addr, port)
#data = sock.recv(128)
