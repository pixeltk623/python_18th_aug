from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	#return HttpResponse("Hello, world. You're at the ERP index.")
	return render(request, 'erp/index.html')

def about(request):
	return render(request, 'erp/about.html')

def contact(request):
	return render(request, 'erp/contact.html')

def courseDetails(request):
	return render(request, 'erp/course-details.html')

def event(request):
	return render(request, 'erp/event.html')

def courses(request):
	return render(request, 'erp/courses.html')

def pricing(request):
	return render(request, 'erp/pricing.html')

def trainers(request):
	return render(request, 'erp/trainers.html')


