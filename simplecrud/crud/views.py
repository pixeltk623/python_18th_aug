from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Person
from django.contrib import messages

# Create your views here.

def index(request):
	all_data = Person.objects.all()
	print(all_data)
	return render(request, 'index.html', {'data' : all_data})

def create(request):
	return render(request, 'create.html')

def store(request):

	if request.method=='POST':

		print(request.POST)
		fname = request.POST['fname']
		lname = request.POST['lname']
		email = request.POST['email']
		if 'gender' in request.POST:
			gender = request.POST['gender']
		else:
			gender = ''

		if 'hobby' in request.POST:
			hobby = request.POST.getlist('hobby')
			hobby = ",".join(hobby)
		else:
			hobby = ''
		city = request.POST['city']
		p = Person(first_name=fname, last_name=lname,email=email, gender = gender, hobby=hobby,city=city)
		p.save()
		messages.add_message(request, messages.INFO, 'User Has been Created.')
		return redirect('/')


def delete(request,id):
	b = Person.objects.get(pk=id)
	b.delete()
	messages.add_message(request, messages.INFO, 'User Has been Deleted.')
	return redirect('/')


def show(request, id):
	b = Person.objects.get(pk=id)
	print(b)
	return render(request, 'show.html', {'all_data': b})


def edit(request, id):
	b = Person.objects.get(pk=id)
	print(b.hobby)
	return render(request, 'edit.html', {'all_data': b})

def update(request):
	if request.method=='POST':
		b = Person.objects.get(pk=request.POST['uid'])

		b.first_name = request.POST['fname']
		b.last_name = request.POST['lname']
		b.email = request.POST['email']
		if 'gender' in request.POST:
			b.gender = request.POST['gender']
		else:
			b.gender = ''

		if 'hobby' in request.POST:
			hobby = request.POST.getlist('hobby')
			b.hobby = ",".join(hobby)
		else:
			hobby = ''
		b.city = request.POST['city']
		b.save()
	messages.add_message(request, messages.INFO, 'User Has been Updated.')
	return redirect('/')


