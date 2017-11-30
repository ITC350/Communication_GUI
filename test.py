from protocol import Protocol
import array
import struct

mac = '98:D3:32:20:82:CA'

test_config_1 = Protocol(mac, 30)
test_config_1.settings([2, 0, 0, 500, 50, 50])
test_config_1.start()

test_config_2 = Protocol(mac, 30)
test_config_2.settings([2, 0, 0, 500, 50, 50])
test_config_2.disable_abs()
test_config_2.start()

def invoke_test(test_config, recv_size):
    result = b''

    with test_config as tc:
        tc.send()
        while len(result) < recv_size:
            msg += tc.receive()
        print(str(msg))

#msg = array.array('H', msg)
#print(msg.tostring())
