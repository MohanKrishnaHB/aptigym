from rest_framework import viewsets, permissions
from student.models import Student
from student.serializer import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_class = [
        permissions.AllowAny
    ]
