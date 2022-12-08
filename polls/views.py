from rest_framework import viewsets

from .models import Question, Choice
from .serializers import QuestionModelSerializer, ChoiceModelSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    """
    Viewset para el modelo de Question.
    """
    queryset = Question.objects.prefetch_related('choice_set__tag').all()  # SELECT id, question_text, pub_date  FROM polls_question
    serializer_class = QuestionModelSerializer
    permission_classes = []


class ChoiceViewSet(viewsets.ModelViewSet):
    """
    Viewset para el modelo de Choice.
    """
    queryset = Choice.objects.select_related('tag').all()  # se debe utilizar select_related
    serializer_class = ChoiceModelSerializer
    permission_classes = []
