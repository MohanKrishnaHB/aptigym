from rest_framework import serializers
from .models import CategoryLevel1, CategoryLevel2, Question, Options


class CategoryLevel1Serializer(serializers.ModelSeializer):
    class Meta:
        model = CategoryLevel1
        fields = "__all__"


class CategoryLevel2Serializer(serializers.ModelSeializer):
    class Meta:
        model = CategoryLevel2
        fields = "__all__"


class OptionsSerializer(serializers.ModelSeializer):
    class Meta:
        model = Options
        fields = ['id', 'option', 'has_image', 'image', 'is_true']


class QuestionSerializer(serializers.ModelSeializer):
    options = OptionsSerializer(many=True)

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
            'created_on'
        ]

    def create(self, validated_data):
        options = validated_data.pop('options')
        question = Question.objects.create(**validated_data)
        for option in options:
            Options.objects.create(question, **option)
        return question
