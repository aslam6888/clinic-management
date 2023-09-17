from rest_framework import serializers
from .models import Doctor, Department
from django.contrib.auth.models import User

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields =  '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    department = DepartmentSerializer()
    
    class Meta:
        model = Doctor
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        return validated_data