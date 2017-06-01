from django.shortcuts import render,redirect
from .models import User
from django.contrib import messages

def index(request):
	return render(request, 'index.html')
def validate(request):
	username = request.POST.get('username', False)
	email = request.POST.get('email', False)
	password = request.POST.get('password', False)
	confirm_pw = request.POST.get('confirm_pw', False)
	postData = {
	'username': username,
	'email': email,
	'password':password,
	'confirm_pw': confirm_pw
	}
	message = ''
	if User.objects.validate(postData):
		messages.add_message(request, messages.INFO, 'Success! Welcome, ' + username)
		User.objects.create(username=username, email=email, password=password)
		users = User.objects.all()
		context = {
		'users': users
		}
		return render(request, 'success.html', context)	
	else:
		messages.add_message(request, messages.INFO, 'Input is not valid!')
		return redirect('/')
def login(request):
	email = request.POST.get('email', False)
	password = request.POST.get('password', False)
	postData = {
	'email': email,
	'password':password,
	}
	if User.objects.login(postData):
		messages.add_message(request, messages.INFO, 'Success! Welcome, ' + email)
		users = User.objects.all()
		context = {
		'users': users
		}
		return render(request, 'success.html', context)	
	else:
		messages.add_message(request, messages.INFO, 'username or password is not correct!')
		return redirect('/')	