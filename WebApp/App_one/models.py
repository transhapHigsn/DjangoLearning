from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default = 0)
    nationality = models.CharField(max_length = 150)
    alias = models.CharField(max_length=100)

    def __str__(self):
        self.name = name
