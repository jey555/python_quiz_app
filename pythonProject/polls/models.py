import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
# each model is represented by a class that subclasses django.db.Model each model has a number of class variable
# each of which represent a database field in the model
# eac field is repeesented b an instance of a Field class ex : CharField, DateTimeFiels
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question_text = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self): return self.choice_text


# how do we activating models ---> a small code gives Djanfo a lots of information which Django is able to
# - create a database schema (CREATE TABLE ) for this app
# - create a python database access API for accesing questions and choice

# 1.30 p.m --------------> introducting the Django Admin
