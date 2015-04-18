from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)


class Horse(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    breeder = models.CharField(max_length=255)
    identity = models.CharField(max_length=255)
    birthday = models.DateField()
    father = models.ForeignKey('self')
    mother = models.ForeignKey('self')
    category = models.ForeignKey('Category')


class Log(models.Model):
    date = models.DateField()
    user = models.ForeignKey(User)
    description = models.TextField()
    # TODO: category, sub-category/details, results
