from rest_framework import serializers
from app1.models import User, salary


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = salary
        fields = '__all__'
