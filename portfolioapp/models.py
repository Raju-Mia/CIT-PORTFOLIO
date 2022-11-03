from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class AboutMe(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about_me = models.TextField(max_length = 500)

    def __str__(self):
        return self.user

class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 500)

    def __str__(self):
        return self.name

class Interest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 250)

    def __str__(self):
        return self.name

class Award(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 250)

    def __str__(self):
        return self.name


class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name_of_institution = models.CharField(max_length = 250)
    passing_year = models.DateField()
    department = models.CharField(max_length = 250)
    name_of_degree = models.CharField(max_length = 250)

    def __str__(self):
        return self.name_of_institution
 
    
class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name_of_company = models.CharField(max_length = 250)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    designation = models.CharField(max_length = 250)
    description = models.TextField()

    def __str__(self):
        return self.user
