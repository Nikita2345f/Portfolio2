from django.shortcuts import render, redirect
from .models import Articels
from .form import ArticelsForm
from django.views.generic import DetailView, UpdateView, DeleteView

def news_homes(request):
    news = Articels.objects.order_by('-date')
    return render(request, 'news/news_homes.html', {'news':news})

class NewsUpdateView(UpdateView):
    model = Articels
    template_name = 'news/create.html'

    form_class = ArticelsForm

class NewsDeleteView(DeleteView):
    model = Articels
    success_url = '/news/'
    template_name = 'news/delete.html'

class NewsDatailView(DetailView):
    model = Articels
    template_name = 'news/datail_view.html'
    context_object_name = 'articles'

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticelsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_homes')
        else :
            error = 'Форма заполнена неверно!'

    form = ArticelsForm()
    date =  {
        'form' : form,
        'error' : error
    }
    return render(request, 'news/create.html',date)