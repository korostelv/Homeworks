from rest_framework import serializers
from .models import Divination


class DivinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Divination
        fields = '__all__'
