from rest_framework import viewsets, permissions
from .models import CategoryLevel1, CategoryLevel2, Question, Options
from .serializer import CategoryLevel1Serializer, CategoryLevel2Serializer, QuestionSerializer, OptionsSerializer


class Category1ViewSet(viewsets.ModelViewSet):
    queryset = CategoryLevel1.objects.all()
    serializer_class = CategoryLevel1Serializer
    permission_class = [
        permissions.AllowAny
    ]


class Category2ViewSet(viewsets.ModelViewSet):
    queryset = CategoryLevel2.objects.all()
    serializer_class = CategoryLevel2Serializer
    permission_class = [
        permissions.AllowAny
    ]


class OptionsViewSet(viewsets.ModelViewSet):
    queryset = Options.objects.all()
    serializer_class = OptionsSerializer
    permission_class = [
        permissions.AllowAny
    ]


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_class = [
        permissions.AllowAny
    ]
