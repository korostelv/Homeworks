import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 11026))

data = client.recv(1024)
print(data.decode('utf-8'))

value = input(': ')
try:
    if value == "n":
        print('Файл отклонен')
        client.send('Файл отклонен.'.encode('utf-8'))
    elif value == 'y':
        print('Файл принимается')
        client.send('Файл принимается.'.encode('utf-8'))

        file = open('new/text.txt', 'wb')
        chunk = client.recv(2048)
        while chunk:
            file.write(chunk)
            chunk = client.recv(2048)
        file.close()

        if not chunk:
            print('Файл загружен')
            client.send('Файл загружен.'.encode('utf-8'))

        client.close()
except:
    print('Введите корректное значение.')
