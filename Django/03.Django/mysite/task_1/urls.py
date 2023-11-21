from rest_framework import routers
from .api import DivinationViewSet
from django.urls import path, include

from .views import future, index

app_name = 'task_1'

router = routers.DefaultRouter()
router.register('api/divination', DivinationViewSet, 'divination')


urlpatterns = [
    path('divination/', include(router.urls)),
    path('future/', future, name='future'),
    path('', index, name='index'),
]

