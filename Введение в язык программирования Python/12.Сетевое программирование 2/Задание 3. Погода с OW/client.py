import  socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost',5022))
data = client.recv(1024)
print(data.decode('UTF-8'))
city = input("Введите название города: ")
client.send(city.encode('utf-8'))

while True:
    data = client.recv(2048)
    if not data:
        break
    print(data.decode('utf-8'))
client.close()


