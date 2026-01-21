from django.db import models

# Create your models here.

class users(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 20)
    role = models.CharField(max_length = 20)

