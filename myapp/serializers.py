from rest_framework import serializers
from .models import *
from datetime import datetime

class StatusSerializer(serializers.ModelSerializer):
            
    class Meta:
        model = Status
        fields ='__all__'
       
