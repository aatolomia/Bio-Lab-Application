from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.

class Student(models.Model):
    YEAR_IN_SCHOOL_CHOICES = (
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
        ('GR', 'Graduate'),
    )
    COURSE_CHOICES = (
        ('Bio', 'Biology'),
        ('CS', 'Computer Science'),
        ('Math', 'Mathematics'),
        ('PS', 'Political Science'),
        ('Psych', 'Psychology'),
        ('Comm', 'Communications'),
        ('FA', 'Fine Arts'),
        ('Mgt', 'Management'),
    )
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    s_number = models.CharField(max_length=20, null=True)
    contact_no = models.CharField(max_length=11)
    email_add = models.CharField(max_length=100)
    s_course = models.CharField(max_length=100, choices=COURSE_CHOICES)
    s_year_lvl = models.CharField(max_length=2, choices=YEAR_IN_SCHOOL_CHOICES)


    def __str__(self):
        if self.first_name and not self.last_name:
            return self.first_name
        elif self.first_name and self.last_name:
            return self.first_name + ' ' + self.last_name
        else:
            return 'Student'


class Class(models.Model):
    c_title = models.CharField(max_length=50)
    c_code = models.CharField(max_length=10, primary_key=True)

    def __str__(self):
        return self.c_title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')
    student_number = models.CharField(max_length=30, null = True)

    def __str__(self):
        return f'{self.user.username} Profile'  

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)