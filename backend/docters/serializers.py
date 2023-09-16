from rest_framework import serializers
from .models import Docter, Department
from django.contrib.auth.models import User

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields =  '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class DocterSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    department = DepartmentSerializer()
    
    class Meta:
        model = Docter
        fields = '__all__'