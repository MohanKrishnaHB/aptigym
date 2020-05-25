from rest_framework import serializers
from .models import *
from question.serializer import QuestionReadOnlySerializer


class TestSetializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = "__all__"


class TestPartitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestPartition
        fields = "__all__"


class TestQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestQuestions
        fields = "__all__"


class TestQuestionsReadOnlySerializer(serializers.ModelSerializer):
    questions = QuestionReadOnlySerializer(many=True, read_only=True)

    class Meta:
        model = TestQuestions
        fields = ['questions']


class TestPartitionReadOnlySerializer(serializers.ModelSerializer):
    questions = TestQuestionsReadOnlySerializer(many=True, read_only=True)

    class Meta:
        model = TestPartition
        fields = ['title', 'description', 'questions']


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
