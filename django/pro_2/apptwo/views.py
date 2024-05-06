from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("<em>My Second app</em>")


def help(request):
    my_dict = {'insert_me': "From the help"}
    return render(request, 'apptwo/index.html', context=my_dict)
