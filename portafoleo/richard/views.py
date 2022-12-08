from django.shortcuts import render

# Create your views here.

from .forms import InputForm

# ...

def form_view(request):
    context = {}
    context['form']= InputForm()
    return render(request, "prueba.html", context)