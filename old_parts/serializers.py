from rest_framework import serializers
from .models import Old_Parts


class Old_PartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Old_Parts
        fields = '__all__'