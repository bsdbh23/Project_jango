from django import forms
from .models import Game 

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields=('name','title_tag','made_by','description','year_of_release','price','author','header_image')
        widgets ={
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag' : forms.TextInput(attrs={'class': 'form-control','placeholder':'This is a Title Placeholder'}),
            'made_by' : forms.TextInput(attrs={'class': 'form-control'}),
            'description' : forms.Textarea(attrs={'class': 'form-control'}),
            'year_of_release' : forms.TextInput(attrs={'class': 'form-control'}),
            'body' : forms.TextInput(attrs={'class': 'form-control'}),
            'author' : forms.Select(attrs={'class': 'form-control'}),
            




        }