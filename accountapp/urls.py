
from django.urls import path, include
from accountapp.views import hello_world_drf
from .views import helloAPI, randomQuiz

urlpatterns = [
    path('hello_world_drf/', hello_world_drf),
    path('hello/', helloAPI),
    path('<int:id>/', randomQuiz),
]
