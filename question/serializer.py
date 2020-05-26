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


class OptionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Options
        fields = ['id', 'question', 'option', 'has_image', 'image', 'is_true']


class OptionsReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = ['id', 'option', 'has_image', 'image']


class QuestionSerializer(serializers.ModelSerializer):
    options = OptionsReadOnlySerializer(many=True, read_only=True)

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
