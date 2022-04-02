from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Question
from .serializers import RandomQuestionSerializer


class RandomQuestion(APIView):

    def get(self, request, format=None):
        #choose = random.choices(Question.objects.db)
        #question =choose[0]
        question = Question.objects.filter().order_by('?')[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)
