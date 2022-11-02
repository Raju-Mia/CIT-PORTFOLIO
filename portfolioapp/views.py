from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

from .models import *

# Create your views here.
def check(request):
    return HttpResponse("app urls setting okay")



def about_me(request,name):
    about_me = AboutMe.objects.get(user__username = name)
    context = {'about_me':about_me}
    return render(request, 'about_me.html', context)