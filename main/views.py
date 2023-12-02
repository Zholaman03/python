from django.shortcuts import render, redirect
from .models import Sentences
from .forms import SentencesForm
from django.views.generic import DeleteView

class TextDelete(DeleteView):
    context_object_name = 'texts'
    model = Sentences
    success_url = '/'
    template_name = 'main/delete.html'

def index(request):
    error = ''
    if request.method == 'POST':
        form = SentencesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Не заполнена'
    forma = SentencesForm()
    data = {
        'title': 'Nurdauletova Akpeil',
        'result': Sentences.objects.all(),
        'form': forma,
        'error': error
    }
    return render(request, "main/index.html", data)

