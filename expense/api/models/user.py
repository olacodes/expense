from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=250, unique=True)
    password = models.CharField(max_length=250, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False)