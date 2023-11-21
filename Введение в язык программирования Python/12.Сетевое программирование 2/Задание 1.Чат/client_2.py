
import socket
import threading

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('localhost',3070))
data = client.recv(1024)
print(data.decode('UTF-8'))


def send_msg():
    while 1:
        msg = input()
        client.sendall((msg).encode('utf-8'))
        if msg == 'exit':
            client.close()
def get_msg():
    while 1:
        data = client.recv(1024)
        if not data:
            break
        print('\n', data.decode('utf-8'))

t1 = threading.Thread(target=send_msg)
t2 = threading.Thread(target=get_msg)
t1.start()
t2.start()