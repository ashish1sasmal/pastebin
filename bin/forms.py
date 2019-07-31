from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Text
import datetime
class RegisterationForm(UserCreationForm):
	email=forms.EmailField(required=True)

	class Meta():
		model=User
		fields=('username','email')

	# def save(self,commit=False):
	# 	user=super(RegisterationForm,self)

class TextForm(forms.ModelForm):
	class Meta():
		model=Text
		exclude=('creator',)


