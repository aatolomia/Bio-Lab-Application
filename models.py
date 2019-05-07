from django.db import models
from datetime import date
from student.models import User
# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Item(models.Model):
    name = models.CharField(max_length=255)
    categories = models.ManyToManyField(Category)
    available = models.IntegerField(default=0)
    picture = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')

class Pending(models.Model):
    user_borrow = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name_of_item = models.CharField(max_length=255)
    num_of_items = models.IntegerField(default=0)
    picture = models.ImageField(default='default.jpg', upload_to='profile_pics')
    date = models.DateField(default=date.today)

class Borrow(models.Model):
    borrower = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name_item = models.CharField(max_length=255)
    num_of_items = models.IntegerField(default=0)
    picture = models.ImageField(default='default.jpg', upload_to='profile_pics')
    date = models.DateField(default=date.today)



