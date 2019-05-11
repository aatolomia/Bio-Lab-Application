from django.db import models
from datetime import date
from student.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self): #specify what to print out
        return self.name

class Item(models.Model):
    categories = models.ManyToManyField(Category)
    #categories = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    available = models.FloatField(default=0)#changes
    name = models.CharField(max_length=255)
    picture = models.ImageField(upload_to = 'profile_pics', blank=False)#changes
    def __str__(self): #specify what to print out
        return self.name

class Pending(models.Model):
    user_borrow =  models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name_of_item = models.CharField(max_length=255)
    num_of_items = models.FloatField(default=0)#changes
    picture = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')
    date = models.DateField(default=date.today)

class Borrow(models.Model):
    borrower =  models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name_item = models.CharField(max_length=255)
    num_of_items = models.FloatField(default=0)#changes
    picture = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')
    date = models.DateField(default=date.today)
