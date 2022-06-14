from contextlib import nullcontext
from operator import truediv
from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

class Photo(models.Model):
    category = models.ForeignKey(category, on_delete=models.CASCADE ,null=True, blank=True)
    # user = models.OneToOneField(User, on_delete=models.CASCADE ,null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    user = models.CharField(max_length=100 , null=True,blank=True)
    description = models.TextField()

    def __str__(self):
        return self.description