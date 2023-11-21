from django.shortcuts import render
import random


def numbers(request):
    if request.method == "POST":
        from_data = int(request.POST.get('from'))
        before_data = int(request.POST.get('before'))
        quant = int(request.POST.get('quant'))
        list = []
        if not from_data or not before_data or not quant:
            text = 'Заполните все колонки'
            return render(request, 'numbers.html', {'text': text})
        if from_data > before_data:
            text = 'Нижний диапазон должен быть меньше верхнего'
            return render(request, 'numbers.html', {'text': text})
        if quant <= 0:
            text = 'Количество должно быть больше 0'
            return render(request, 'numbers.html', {'text': text})
        else:
            for i in range(quant):
                list.append(random.randint(from_data, before_data))
            return render(request, 'numbers.html', {'list':list})
    return render(request, 'numbers.html')