from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from iot.models import *
from iot.serializers import *

# Create your views here.

class getDevices(APIView):
    def get(self,request):
        
        devices = Device.objects.all()
        serializer = DeviceSerializer(devices,many=True)
        context = {"devices":serializer.data}
        return Response(context)