from django.db import models


class Profile(models.Model):
    first_name = models.CharField(max_length=30,)
    last_name = models.CharField(max_length=30,)
    image = models.URLField()


class Book(models.Model):
    title = models.CharField(max_length=20,)
    description = models.TextField()
    picture = models.URLField()
    type = models.CharField(max_length=30)