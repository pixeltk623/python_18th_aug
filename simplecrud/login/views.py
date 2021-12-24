from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
import os
import random
from .models import FileUpload
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

def index(request):
	all_data = FileUpload.objects.all()
	print(all_data)
	return render(request, 'login/index.html', {'data' : all_data})

def create(request):
	return render(request, "login/create.html")

def store(request):

	if request.method=='POST':
		
		name = request.POST['name'];
		fileUpload = request.FILES
		split_tup = os.path.splitext(request.FILES['fileUpload'].name)
		file_name = str(random.randint(4565456,98512365))+split_tup[1]
		handle_uploaded_file(request.FILES['fileUpload'],file_name)
		p = FileUpload(name=name, file=file_name)
		p.save()
		# messages.add_message(request, messages.INFO, 'User Has been Created.')
		return redirect('/login')


def handle_uploaded_file(f, file_name):
	with open('login/static/upload/'+file_name, 'wb+') as destination:
	    for chunk in f.chunks():
	        destination.write(chunk)


def register(request):
	return render(request, "login/register.html")

def registration(request):
	if request.method=='POST':
		first_name = request.POST['first_name'];
		last_name = request.POST['last_name'];
		email = request.POST['email'];
		username = request.POST['username'];
		password = request.POST['password'];

		user = User.objects.create_user(first_name = first_name, last_name = last_name, username = username, email = email, password = password)
		user.save()

		return redirect('/login/login')


def loginReq(request):
	if request.method=='POST':
		username = request.POST['username'];
		password = request.POST['password'];
		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request,user)
			return redirect('/login/profile')
		else:
		    return redirect('/login/login')

	return render(request, "login/login.html")


def profile(request):
	# if request.user.is_authenticated:
	# 	return redirect('/login/profile')
	# else:
	# 	return redirect('/login/login')
	return render(request, "login/profile.html")

	


def logout_view(request):
    logout(request)
    return redirect('/login/login')