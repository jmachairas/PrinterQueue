from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Printer, Job


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')


class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job
        fields = ('jobname', 'description', 'orientation', 'incolor', 'duplex', 'jobid', 'copies', 'priority')


class PrinterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Printer
        fields = ('devicename', 'description', 'colorcapable', 'duplex', 'users', 'deviceid', 'copies')



