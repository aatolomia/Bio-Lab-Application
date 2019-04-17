from django.db import models
from datetime import date
# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Item(models.Model):
    name = models.CharField(max_length=255)
    categories = models.ManyToManyField(Category)
    available = models.IntegerField(default=0)



class Borrow(models.Model):
    item = models.ManyToManyField(Item)
   # student = models.ManyToManyField(Student)
    qty = models.IntegerField(default=0)
    date = models.DateField(default=date.today)
    status = models.CharField(max_length=25)
