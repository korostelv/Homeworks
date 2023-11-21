from django.shortcuts import render

# Create your views here.
def numbers(request):
    if request.method == 'POST':
        one = int(request.POST.get('number_1'))
        two = int(request.POST.get('number_2'))
        three = int(request.POST.get('number_3'))
        action = request.POST.get('numb')
        list = [one, two, three]
        if action == 'min':
            text = f'Минимальное число: {min(list)}'
        elif action == 'max':
            text = f'Максимальное число: {max(list)}'
        elif action == 'average':
            text = f'Среднеарифметическое чисел: {(one + two + three)/3}'
        return render(request, "numbers.html", {'text':text})


    return render(request, "numbers.html")