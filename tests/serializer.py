from rest_framework import serializers
from .models import *
from question.serializer import QuestionSerializer


class TestSetializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = "__all__"


class TestPartitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestPartition
        fields = '__all__'


class TestQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestQuestions
        fields = ['partition', 'question']


class StudentTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentTest
        fields = '__all__'


class StudentQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentQuestion
        fields = '__all__'


class StudentQuestionOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentQuestionOption
        fields = '__all__'
