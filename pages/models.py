from django.db import models

# Create your models here.

class index(models.Model):
    title = models.CharField(max_length=15)