from rest_framework import serializers
from .models import *


class PotSerializer(serializers.ModelSerializer):
    class MetaData:
        model = Pot
        fields = '__all__'


class PlantInfoSerializer(serializers.ModelSerializer):
    class MetaData:
        model = PlantInfo
        fields = '__all__'
