from rest_framework import viewsets, permissions
from .models import Divination
from .serializers import DivinationSerializer


class DivinationViewSet(viewsets.ModelViewSet):
    queryset = Divination.objects.all()
    # permission_classes = [permissions.AllowAny]
    serializer_class = DivinationSerializer
