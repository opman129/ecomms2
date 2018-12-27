from django.db import models

# Create your models here.
class Login(models.Model):
    Username    = models.Charfield(blank=False)
    password    = models.Charfield(blank=False)