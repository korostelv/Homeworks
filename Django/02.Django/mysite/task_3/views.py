from django.shortcuts import render
from .forms import AddUser
from .models import User


def shop(request):
    if request.method == 'POST':
        form = AddUser(request.POST)
        if form.is_valid():
            user = form.save()
            return render(request, 'users_shop.html', {'user': user})
    else:
        form = AddUser()
    return render(request, "shop.html", {'form': form})


def users_shop(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'users_shop.html', {'user': user})
