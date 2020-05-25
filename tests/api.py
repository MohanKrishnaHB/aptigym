from rest_framework import viewsets, permissions
from .models import *
from .serializer import *


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSetializer
    permission_class = [
        permissions.AllowAny
    ]


class TestPartitionViewSet(viewsets.ModelViewSet):
    queryset = TestPartition.objects.all()
    serializer_class = TestPartitionSerializer
    permission_class = [
        permissions.AllowAny
    ]


class TestQuestionsViewSet(viewsets.ModelViewSet):
    queryset = TestQuestions.objects.all()
    serializer_class = TestQuestionsSerializer
    permission_class = [
        permissions.AllowAny
    ]


class TestPartitionReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TestPartition.objects.all()
    serializer_class = TestPartitionReadOnlySerializer
    permission_class = [
        permissions.AllowAny
    ]


class StudentTestViewSet(viewsets.ModelViewSet):
    queryset = StudentTest.objects.all()
    serializer_class = StudentTestSerializer
    permission_class = [
        permissions.AllowAny
    ]


class StudentQuestionViewSet(viewsets.ModelViewSet):
    queryset = StudentQuestion.objects.all()
    serializer_class = StudentQuestionSerializer
    permission_class = [
        permissions.AllowAny
    ]


class StudentQuestionOptionViewSet(viewsets.ModelViewSet):
    queryset = StudentQuestionOption.objects.all()
    serializer_class = StudentQuestionOptionSerializer
    permission_class = [
        permissions.AllowAny
    ]
