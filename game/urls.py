from django.urls import path
from .views import HomeView
from .views import GameDetailsView
from .views import AddGameView
urlpatterns = [
    path('',HomeView.as_view(), name="home"),
    path('game/<int:pk>',GameDetailsView.as_view(), name="game_details"),
    path('add_game/',AddGameView.as_view(), name="add_game"),

]