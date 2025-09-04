# usuarios/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import PerfilUsuario

class PerfilUsuarioSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)

    class Meta:
        model = PerfilUsuario
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'unidad', 'cargo']