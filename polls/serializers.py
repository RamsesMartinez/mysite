from rest_framework import serializers

from polls.models import Question, Choice, ChoiceTag


class ChoiceTagModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceTag
        fields = '__all__'

class ChoiceModelSerializer(serializers.ModelSerializer):
    """Serializer para las opciones de las preguntas"""
    tag = ChoiceTagModelSerializer()
    class Meta:
        model = Choice
        fields = '__all__'


class QuestionModelSerializer(serializers.ModelSerializer):
    """Serializer para las preguntas"""
    choices = ChoiceModelSerializer(source="choice_set", many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'pub_date', 'choices']

