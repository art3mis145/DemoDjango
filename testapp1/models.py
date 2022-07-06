from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField('Ho Ten', max_length=200)
    mssv = models.BigIntegerField('MaSV')
    bday = models.DateTimeField('Ngay sinh')
