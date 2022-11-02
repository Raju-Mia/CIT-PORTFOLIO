from django.urls import path

from . import views 

urlpatterns = [
    path('check/', views.check, name='check'),
    path('<name>/about-me/', views.about_me, name='about-me'), #dynamic url pass for get data.

]