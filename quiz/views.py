from django.db.models import F
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Question, Score
from .serializers import RandomQuestionSerializer, ScoreSerializer
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class RandomQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        question = Question.objects.order_by('?')[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)


class UpdateScores(APIView):

    def post(self, request, format=None):
        serializer = ScoreSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data['name']
            points = serializer.validated_data['points']

            if Score.objects.filter(name=name).exists():
                serializer = Score.objects.get(name=name)
                serializer.points = F('points') + points
                if points <= 0:
                    serializer.points = int(0)
                serializer.save()

            return Response(None, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Leaderboard(APIView):

    def get(self, request, format=None):
        scores = Score.objects.all().order_by('-points')[:10]
        serializer = ScoreSerializer(scores, many=True)
        return Response(serializer.data)