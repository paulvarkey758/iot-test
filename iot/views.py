from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from iot.models import *

# Create your views here.

class getDevices(APIView):
    def get(self,request):
        
        devices = Device.objects.all()
        device1 = devices[0]

        return Response(device1.value)