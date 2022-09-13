from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class IrisModel(models.Model):
    
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    sepal_length = models.IntegerField(null = True, blank=True)
    sepal_width = models.IntegerField(null = True, blank=True)
    petal_length = models.IntegerField(null = True, blank=True)
    petal_width = models.IntegerField(null = True, blank=True)