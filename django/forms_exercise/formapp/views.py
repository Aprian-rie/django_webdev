from django.shortcuts import render
from . import forms


# Create your views here.

def index_view(request):
    return render(request, "index.html")


def form_view(request):
    form = forms.MyForm()
    return render(request, "form_page.html", {'form': form})
