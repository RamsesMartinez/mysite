from rest_framework import serializers

from polls.models import Question, Choice


class ChoiceModelSerializer(serializers.ModelSerializer):
    """Serializer para las opciones de las preguntas"""
    class Meta:
        model = Choice
        fields = '__all__'


class QuestionModelSerializer(serializers.ModelSerializer):
    """Serializer para las preguntas"""
    choices = ChoiceModelSerializer(source="choice_set", many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'pub_date', 'choices']

