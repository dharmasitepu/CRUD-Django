from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields import IntegerField

# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class maha(models.Model):
    nama = models.CharField(max_length=100)
    NIM = models.IntegerField()
    kelas = models.CharField(max_length=100)
    jkelamin = models.ForeignKey(Position,on_delete=models.CASCADE)