import socket
import threading

def weather(city):
    with open('weather.txt','r',encoding='utf-8') as f:
        lst = f.read().split('\n')
    for i in range(len(lst)):
        if lst[i] == city:
            lst2 = lst[i:i+27]
    lst3 = []
    for i in lst2:
        lst3.append(i+'\n')
    text = ' '.join(lst3)
    return text


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost',6020))
server.listen()
def accept():
    conn , addr = server.accept()
    print('Подключение к ',addr)
    conn.sendall('Вы подключены'.encode('UTF-8'))
    threading.Thread(target=accept).start()
    data = conn.recv(1024)
    city = data.decode('utf-8')
    text = weather(city)
    conn.sendall(text.encode('utf-8'))

accept()