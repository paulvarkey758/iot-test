from rest_framework import serializers
from iot.models import *

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id','name','value']