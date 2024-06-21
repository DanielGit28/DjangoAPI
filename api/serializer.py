from rest_framework import serializers
from .models import *

class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta: 
        model=Programmer
        #fields = ('fullname', 'nickname','')
        fields = '__all__'
        

class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = React
        fields = ['employee', 'department']