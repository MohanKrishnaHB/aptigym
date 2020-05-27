from rest_framework import serializers
from .models import *
from question.serializer import QuestionSerializer


class TestPartitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestPartition
        fields = '__all__'


class TestSetializer(serializers.ModelSerializer):
    partitions = TestPartitionSerializer(read_only=True, many=True)

    class Meta:
        model = Test
        fields = [
            'title',
            'description',
            'no_of_questions',
            'partitions',
            'total_duration',
            'negative_marking',
            'commence_at',
            'stop_commenceing_after',
            'show_score',
            'show_answers'
        ]


class TestQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestQuestions
        fields = ['partition', 'question']


class StudentTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentTest
        fields = '__all__'


class StudentQuestionOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentQuestionOption
        fields = '__all__'


class StudentQuestionSerializer(serializers.ModelSerializer):
    option = StudentQuestionOptionSerializer(read_only=True, many=True)

    class Meta:
        model = StudentQuestion
        fields = [
            'id',
            'student',
            'question',
            'option',
            'status',
            'points',
            'duration'
        ]
