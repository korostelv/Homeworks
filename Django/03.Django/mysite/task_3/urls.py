
from rest_framework import routers
from .api import PoemViewSet, AuthorViewSet, ThemeViewSet
from django.urls import path, include, re_path
from .views import poetry, stych, catalog, crambo

app_name = 'task_3'

router = routers.DefaultRouter()
router.register('poem', PoemViewSet, 'poem')
router.register('author', AuthorViewSet, 'author')
router.register('theme', ThemeViewSet, 'theme')

urlpatterns = [
    path('api/', include(router.urls)),
    path('poetry', poetry, name='poetry'),
    path('stych', stych, name='stych'),
    path('catalog', catalog, name='catalog'),
    path('crambo/<int:poem_id>/', crambo, name='crambo'),
]



