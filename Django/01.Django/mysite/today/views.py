from django.shortcuts import render
from datetime import datetime, timedelta

date = datetime.now().strftime('%d-%m-%Y')

list_table = []
count = 1
for i in range(2, 10):
    for j in range(2, 10):
        count += 1
        list_table.append(f'{i} * {j} = {i * j}')
        if j == 9:
            list_table.append(' ')


current_date = datetime.now()
first_day_of_year = datetime(current_date.year, 1, 1)
prog_day = (first_day_of_year + timedelta(days=255)).strftime('%d-%m-%Y')


def index(request):
    return render(request,'index.html')


def today(request):
    return render(request,'today.html',{'date':date})


def table(request):
    return render(request, 'table.html', {'list_table':list_table})


def progday(request):
    return render(request, 'progday.html', {'prog_day':prog_day})
