from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Question
from .serializers import RandomQuestionSerializer
from django.views.generic import TemplateView

class RandomQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        question = Question.objects.order_by('?')[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)


class IndexView(TemplateView):
    
    template_name = 'index.html'

