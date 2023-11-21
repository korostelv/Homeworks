from django.urls import path

from .views import day_prog

app_name ='task_4'

urlpatterns = [
    path('day_prog/', day_prog, name="day_prog"),

]