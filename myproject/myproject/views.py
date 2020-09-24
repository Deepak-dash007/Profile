from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	return render(request, 'index.html')

def about(request):
	return render(request, 'about.html')

def career(request):
	return render(request, 'career.html')

def projects(request):
	return render(request, 'projects.html')

def education(request):
	return render(request, 'education.html')

def contact(request):
	return render(request, 'contact.html')