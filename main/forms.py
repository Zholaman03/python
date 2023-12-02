from .models import Sentences
from django.forms import ModelForm, TextInput

class SentencesForm(ModelForm):
    class Meta:
        model = Sentences
        fields = ['title']

        widgets= {
            'title': TextInput(attrs={
                'class': 'form-control w-100',
                'placeholder': 'Текст который хотела что писать'
            })
        }