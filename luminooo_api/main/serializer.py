from rest_framework import serializers
from .import models


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = '__all__'
        # fields = ['id','full_name', 'date_of_birth', 'email', 'password', 'qualification', 'mobile_number', 'address', 'subject']