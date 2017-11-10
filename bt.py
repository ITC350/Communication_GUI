import bluetooth

max_data_size = 128

def open_bt(mac_addr, port):
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM).connect((mac_addr, port))

    try:
        client, clientInfo = s.accept()
        return (sock, client, client_info)

    except:
        return None

def close_bt(bt):
    bt.close()

def send_msg(bt, msg):
    bt.send(msg)

def receive_msg(bt, msg, size = max_data_size):
    return bt.recv(size)


