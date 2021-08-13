from rest_framework import serializers
from .models import Agenda


class AgendaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = ['__all__']


class AgendaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = ['__all__']
