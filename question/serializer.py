from rest_framework import serializers
from .models import CategoryLevel1, CategoryLevel2, Question, Options


class CategoryLevel1Serializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryLevel1
        fields = "__all__"


class CategoryLevel2Serializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryLevel2
        fields = "__all__"


class QuestionReadOnlySerializer(serializers.ModelSerializer):
    options = OptionsSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = [
            'id',
            'question',
            'has_question_image',
            'question_image',
            'options',
            'solution',
            'has_solution_image',
            'solution_image',
            'category'
        ]


class OptionsSerializer(serializers.ModelSerializer):
    # question = QuestionReadOnlySerializer(read_only=True)

    class Meta:
        model = Options
        fields = ['id', 'question', 'option', 'has_image', 'image', 'is_true']


class QuestionSerializer(serializers.ModelSerializer):
    options = OptionsSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = [
            'id',
            'question',
            'has_question_image',
            'question_image',
            'options',
            'solution',
            'has_solution_image',
            'solution_image',
            'category'
        ]
