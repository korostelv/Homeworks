import socket
import threading

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('localhost',5052))
data = client.recv(1024)
print(data.decode('UTF-8'))
login = input('Введите логин: ')
client.sendall(login.encode('utf-8'))
passw = input('Введите пароль: ')
client.sendall(passw.encode('utf-8'))

def send_msg():
    while 1:
        msg = input()
        client.sendall((login+':'+msg).encode('utf-8'))

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
