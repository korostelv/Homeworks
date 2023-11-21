from django.shortcuts import render
from datetime import datetime, timedelta

def day_prog(request):
    if request.method == 'POST':
        year = int(request.POST.get('year'))
        first_day_of_year = datetime(year, 1, 1)
        prog_day = (first_day_of_year + timedelta(days=255)).strftime('%d %B (%A)')
        print(prog_day)
        return render(request, "day_prog.html", {'prog_day': prog_day,'year': year})

    return render(request, "day_prog.html")
