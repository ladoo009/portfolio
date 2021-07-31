from django.db import models


class Intex(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()