from django.urls import path, include

from .views import numbers

app_name = 'task_2'

urlpatterns = [
    path('numbers/', numbers, name='numbers'),
]
