from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	first_name = forms.CharField()
	last_name = forms.CharField()
	student_number = forms.CharField(max_length = 20)
	

	class Meta:
		model = User 
		fields = ['username', 'email', 'first_name', 'last_name', 'student_number', 'password1', 'password2']
