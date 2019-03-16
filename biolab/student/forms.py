from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'style':'max-width: 20em'}))
	email = forms.EmailField(widget=forms.TextInput(attrs={'style':'max-width: 20em'}))
	first_name = forms.CharField(widget=forms.TextInput(attrs={'style':'max-width: 20em'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'style':'max-width: 20em'}))
	student_number = forms.CharField(max_length = 20, widget=forms.TextInput(attrs={'style':'max-width: 20em'}))
	

	class Meta:
		model = User 
		fields = ['username', 'email', 'first_name', 'last_name', 'student_number', 'password1', 'password2']
		
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'style':'max-width: 20em'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'style':'max-width: 20em'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
