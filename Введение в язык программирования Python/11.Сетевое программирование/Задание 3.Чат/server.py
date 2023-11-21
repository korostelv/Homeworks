
import socket
import threading

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('localhost',5052))
server.listen(3)

clients = []
pw = {'qwerty':'12345','val':'val','ted':'ted'}
pw_client = {}

def accept():
    user, addr = server.accept()
    clients.append(user)
    print('Подключен к',addr)
    user.sendall('Вы подключены'.encode('UTF-8'))
    threading.Thread(target=accept).start()

    login = user.recv(1024)
    passw = user.recv(1024)
    pw_client[login.decode('utf-8')] = passw.decode('utf-8')

    if login.decode('utf-8') not in pw or (pw[login.decode('utf-8')] != passw.decode('utf-8')):
        user.sendall('Логин и(или) пароль не верны.'.encode('UTF-8'))
        user.close()

    user.sendall('Вы авторизованы.'.encode('UTF-8'))

    while True:
        data = user.recv(1024)
        print(data.decode('UTF-8'))
        for i in clients:
            if i != user:
                i.sendall(data)


accept()


