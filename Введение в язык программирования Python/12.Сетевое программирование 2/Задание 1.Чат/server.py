
import socket
import threading


server =  socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('localhost',3070))
server.listen()
print('Ожидание подключения')
clients = []


def accept():
    while True:
        if len(clients) < 2:
            conn, addr = server.accept()
            clients.append(conn)
            print(f"Соединение установлено к {addr}, количество подключений: {len(clients)}")
            conn.sendall('Вы подключены'.encode('utf-8'))
            threading.Thread(target=accept).start()
            while True:
                data = conn.recv(1024)
                print(data.decode('utf-8'))
                if data.decode('utf-8') == 'exit':
                    clients.remove(conn)
                    print(f"количество подключений: {len(clients)}")
                    conn, addr = server.accept()
                    clients.append(conn)
                    print(f"Соединение установлено к {addr}, количество подключений: {len(clients)}")
                    conn.sendall('Вы подключены'.encode('utf-8'))
                for i in clients:
                    if i != conn:
                        i.send(data)

# t1 = threading.Thread(target=accept).start()
# t2 = threading.Thread(target=accept).start()

accept()







