from django.urls import path

from . import views 

urlpatterns = [
    path('check/', views.check, name='check'),
    path('<name>/',views.home, name='home'),
    path('<name>/about-me', views.about_me, name='about-me'), #dynamic url pass for get data.
    path('<name>/skill', views.skill, name='skill'),
    path('<name>/intarest', views.intarest, name='intarest'),
    path('<name>/award', views.award, name='award'),
    path('<name>/education/', views.education, name='education'),
    path('<name>/exprience/', views.exprience, name='exprience'),

]