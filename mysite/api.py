from rest_framework import routers

from polls.views import QuestionViewSet, ChoiceViewSet


# Para Desarrollo
router = routers.DefaultRouter()

# Para Producción
# router = routers.SimpleRouter()


router.register('polls/questions', QuestionViewSet, basename='questions')
router.register('polls/choices', ChoiceViewSet, basename='choices')
