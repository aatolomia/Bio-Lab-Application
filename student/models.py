from django.db import models

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
	s_name = models.CharField(max_length=100)
	s_number = models.CharField(max_length=20, primary_key=True)
	contact_no = models.CharField(max_length=11)
	email_add = models.CharField(max_length=100)
	s_course = models.CharField(max_length=100, choices=COURSE_CHOICES)
	s_year_lvl = models.CharField(max_length=2, choices=YEAR_IN_SCHOOL_CHOICES)
	
class Class(models.Model):
	c_title = models.CharField(max_length=50)
	c_code = models.CharField(max_length=10,primary_key=True)
	
	
	