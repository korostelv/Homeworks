import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 11026))
server.listen()
conn, addr = server.accept()
print('Подключение к ', addr)
conn.send('Вы готовы принять файл?(Y/N)?'.encode('utf-8'))

data = conn.recv(1024)
print(data.decode('utf-8'))

file = open('old/text.txt', 'rb')
file_data = file.read(2048)
while file_data:
    conn.send(file_data)
    file_data = file.read(2048)
file.close()
# data = conn.recv(1024)
# print(data.decode('utf-8'))
conn.close()
