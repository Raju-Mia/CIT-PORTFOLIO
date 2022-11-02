from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

from .models import *

# Create your views here.
def check(request):
    return HttpResponse("app urls setting okay")



def about_me(request,name):
    about_mee = AboutMe.objects.get(user__username = name)
    context = {'about_m':about_mee}
    return render(request, 'about_me.html', context)


def skill(request,name):
    skillss = Skill.objects.filter(user__username = name)
    context = {'skills': skillss}
    return render(request, 'skill.html', context)

def intarest(request,name):
    intarestes = Interest.objects.filter(user__username = name)
    context = {'intarests': intarestes}
    return render(request, 'intarest.html', context)



def award(request,name):
    awardes = Award.objects.filter(user__username = name)
    context = {'awards': awardes}
    return render(request, 'award.html', context)


def education(request,name):
    pass



def exprience(request,name):
    pass
