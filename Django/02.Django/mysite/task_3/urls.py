from django.urls import path

from .views import shop, users_shop

app_name ='task_3'

urlpatterns = [
    path('shop/', shop, name="shop"),
    path('users_shop/<int:user_id>/', users_shop, name="users_shop"),
]