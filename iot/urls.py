from django.urls import path
from iot.views import *

urlpatterns = [
    path('getdata/',getDevices.as_view()),
]