from rest_framework import viewsets, permissions
from .models import Poem, Author, Theme
from .serializers import PoemSerializer, AuthorSerializer, ThemeSerializer


class PoemViewSet(viewsets.ModelViewSet):
    queryset = Poem.objects.all()
    serializer_class = PoemSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class ThemeViewSet(viewsets.ModelViewSet):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer
