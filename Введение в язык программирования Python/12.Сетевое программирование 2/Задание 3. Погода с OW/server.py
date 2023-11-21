import socket
import requests
import math
import threading


def weather(city):
    API_KEY = '04b61c250623ebba8e31feb298cbda1d'
    open_weather = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric&lang=ru&"
    data = requests.get(open_weather).json()
    list = []
    list.append(f"Прогноз погоды в городе {city} днем:")
    for i in data['list']:
        if i['dt_txt'][11:] == "15:00:00":
            list.append(f"\nДата: {i['dt_txt'][:10]}")
            list.append(f"\n\tТемпература: {math.trunc(i['main']['temp'])} гр.С")
            list.append(f"\n\tCкорость ветра: {math.trunc(i['wind']['speed'])} м/с")
            if i['wind']['deg'] >= 0 and i['wind']['deg'] < 45:
                list.append('\n\tНаправление ветра: C')
            elif i['wind']['deg'] >= 45 and i['wind']['deg'] < 90:
                list.append('\n\tНаправление ветра: C-В')
            elif i['wind']['deg'] >= 90 and i['wind']['deg'] < 135:
                list.append('\n\tНаправление ветра: В')
            elif i['wind']['deg'] >= 135 and i['wind']['deg'] < 180:
                list.append('\n\tНаправление ветра: Ю-В')
            elif i['wind']['deg'] >= 180 and i['wind']['deg'] < 225:
                list.append('\n\tНаправление ветра: Ю')
            elif i['wind']['deg'] >= 225 and i['wind']['deg'] < 270:
                list.append('\n\tНаправление ветра: Ю-З')
            elif i['wind']['deg'] >= 270 and i['wind']['deg'] < 315:
                list.append('\n\tНаправление ветра: З')
            else:
                list.append('\n\tНаправление ветра: С-З')
            list.append(f"\n\tОсадки: {i['weather'][0]['description']}")
    text = ''.join(list)
    return text



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost',5022))
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