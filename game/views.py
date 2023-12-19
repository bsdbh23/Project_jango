from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from .models import Game
from .forms import GameForm

# Create your views here.
#def home(request):
#    return render(request, 'home.html',{})

class HomeView(ListView):
    model = Game
    template_name = 'home.html'


class GameDetailsView(DetailView):
    model = Game 
    template_name= 'game_details.html'   

class  AddGameView(CreateView):
    model = Game
    form_class =GameForm
    template_name = 'add_game.html'
    #fields = '__all__'