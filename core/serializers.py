from rest_framework import serializers
from .models import User
from rest_framework import serializers
from .models import Department, Employee, Achievement, AchievementEmployee

#User Registration Serializers
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    re_password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 're_password')

    def validate(self, attrs):
        if attrs['password'] != attrs['re_password']:
            raise serializers.ValidationError(
                {'password': 'Password fields didn\'t match.'})
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user



#Employee Serializers

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name']

class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ['id', 'name']

class AchievementEmployeeSerializer(serializers.ModelSerializer):
    employee = serializers.StringRelatedField(source='employee.name')
    achievement = serializers.StringRelatedField(source='achievement.name')

    class Meta:
        model = AchievementEmployee
        fields = ['achievement','employee', 'achievement_date']




class EmployeeSerializer(serializers.ModelSerializer):
    achievements = serializers.PrimaryKeyRelatedField(many=True, queryset=Achievement.objects.all(), required=False)

    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'phone', 'address', 'department', 'achievements']



