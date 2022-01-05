from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.

def index(request):
	return render(request, 'cepms/index.html')

def login(request):
	return render(request, 'cepms/login.html')

def register(request):
	return render(request, 'cepms/register.html')



def main(request):
	if request.method=='POST':
		status = send_mail(
			request.POST['subject'],
			request.POST['message'],
			'sharvank1515@gmail.com',
			[request.POST['email']],
			fail_silently=False,
		)

		print(status)
		messages.add_message(request, messages.INFO, 'Email has been sent')
	return render(request, 'frontEnd/index.html')