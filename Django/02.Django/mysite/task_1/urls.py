from django.urls import path

from .views import form, user, index

# from . import views


app_name ='task_1'

urlpatterns = [
    path('', index, name="index"),
    path('form/', form, name="form"),
    path('user/', user, name="user"),
]