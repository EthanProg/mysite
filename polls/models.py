import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
"""
    The code is straightforward. Each model is represented by a class
    that subclasses django.db.models.Model. Each model has a number of
    class variables, each of which represents a database field in the model.
"""


class Question(models.Model):
    """
        Each field is represented by an instance of a Field class – e.g.,
        CharField for character fields and DateTimeField for datetimes.
        This tells Django what type of data each field holds.
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateField('date published')

    def _str_(self):
        """
            It’s important to add __str__() methods to your models,
            not only for your own convenience when dealing with the
            interactive prompt, but also because objects’ representations
            are used throughout Django’s automatically-generated admin.
        """
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text