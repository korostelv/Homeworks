from django.shortcuts import render
import requests
import random


def future(request):
    if request.method == "POST":
        link = 'http://127.0.0.1:8000/divination/api/divination/?format=json'
        divination = requests.get(link).json()
        random_index = random.randint(0, (len(divination) - 1))
        prediction = divination[random_index]['prediction']
        return render(request, 'future.html', {'prediction': prediction})
    return render(request, 'future.html')


def index(request):
    return render(request,'index.html')


