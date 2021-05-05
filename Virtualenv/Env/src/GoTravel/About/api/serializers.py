from rest_framework import serializers
from ..models import About, SubDescription

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model=About
        fields='__all__'

class SubDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model=SubDescription
        fields='__all__'
