from django.shortcuts import render
from . import forms

# Create your views here.

def index(request):
    return render(request, 'formsapp/index.html')

def form_name_view(request):
    form = forms.FormName()
    return render(request, 'formsapp/form_page.html', {'form': form})
