from django.db import models

# Create your models here.


class home(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()

