from rest_framework import serializers
from .models import Auto_Roof


class Auto_RoofSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auto_Roof
        fields = '__all__'