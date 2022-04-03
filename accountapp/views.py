from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz
from .serializers import QuizSerializer
import random

def hello_world(request):
    return render(request, 'accountapp/temp.html')

@api_view()
def hello_world_drf(request):
    return Response({'message': 'Hello_world!'})

@api_view()
def helloAPI(request):
    return Response("hello world!")

@api_view()
def randomQuiz(request, id):
    totalQuizs = Quiz.objects.all()
    randomQuizs = random.sample(list(totalQuizs), id)
    serializer = QuizSerializer(randomQuizs, many=True)
    return Response(serializer.data)