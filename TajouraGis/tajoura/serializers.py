# tajoura/serializers.py

from rest_framework import serializers
from .models import School, AcademicLevel, CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id','first_name','last_name', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    

class UserMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff')


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff')




class AcademicLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicLevel
        fields = '__all__'

class SchoolSerializer(serializers.ModelSerializer):
    academic_levels = AcademicLevelSerializer(many=True, read_only=True)

    class Meta:
        model = School
        fields = '__all__'

class CreateSchoolWithLevelsSerializer(serializers.Serializer):
    schools = SchoolSerializer(many=True)
    academic_levels = AcademicLevelSerializer(many=True)