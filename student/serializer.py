from rest_framework import serializers
from student.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'register_number', 'first_name',
                  'last_name', 'email', 'phone_number']
