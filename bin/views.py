from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate,logout
from datetime import date
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect 
from .models import Text

from django.contrib.auth.models import User
from .forms import *
# Create your views here.
def index(request):
	return render(request,'bin/index.html')

def register(request):
	registered=False
	if request.method=='POST':
		user_form=UserForm(data=request.POST)
		if user_form.is_valid():
			user=user_form.save()
			user.set_password(user.password)
			# User.objects.create_user(**user.cleaned_data)
			user.save()
			registered=True

	else:
		user_form=UserForm()
	return render(request,'bin/registeration.html',{'user_form':user_form,'registered':registered})

@login_required
def paste(request):
	if request.method=='POST':
		text_input=TextForm(data=request.POST)
		if text_input.is_valid():
			# text_input.creator=request.user
			obj=text_input.save(commit=False)
			obj.creator=request.user
			obj.save()
			# text_input.save()
			return HttpResponseRedirect(reverse('index'))
			

	else:
		text_input=TextForm()
		return render(request,'bin/paste.html',{'text_input':text_input})

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))

def user_login(request):
	if request.method=='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')

		user=authenticate(username=username,password=password)
		print(username,password,user)
		if user:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect(reverse('index'))
				print("login successful!")
			else:
				return HttpResponse('User not active')

		else:
			return HttpResponse("Enter valid details !!")

	else:
		return render(request,'bin/login.html',{})


@login_required
def paste_list(request):
	f=Text.objects.all()
	return render(request,'bin/paste_list.html',{'f':f,'u':[request.user]})
	
