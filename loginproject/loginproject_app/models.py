from django.db import models

class LoginDetails(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobilenumber = models.CharField(max_length=15)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name


