from django.db import models


class Person(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    age = models.IntegerField(default=18)


