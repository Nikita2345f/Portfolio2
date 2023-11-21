from .models import Articels
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticelsForm(ModelForm):
    class Meta: 
        model = Articels
        fields = [ 'title', 'anons', 'stt', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Название статьи'
            }),
            "anons" : TextInput(attrs={
                'class' : 'form-control', 
                'placeholder' : 'Анонс'
            }),
            "date" : DateTimeInput(attrs={
                'class' : 'form-control', 
                'placeholder' : 'Дата'
            }),
            "stt" : Textarea(attrs={
                'class' : 'form-control', 
                'placeholder' : 'Текст статьи'
            }),

        } 