from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
import os
import random
from .models import FileUpload

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
