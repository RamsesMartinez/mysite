from rest_framework import viewsets

from .models import Question
from .serializers import QuestionModelSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Question.objects.all()  # SELECT id, question_text, pub_date  FROM polls_question
    serializer_class = QuestionModelSerializer
    permission_classes = []
