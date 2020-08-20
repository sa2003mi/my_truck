from rest_framework import serializers
from .models import Spare_Parts


class Spare_PartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spare_Parts
        fields = '__all__'