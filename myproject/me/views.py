from django.http import HttpResponse
from django.shortcuts import render
from .models import Experience, project, PageView
from django.template.loader import get_template
from .forms import MessageForm


def index(request):
	p = PageView()
	p.page = "about"
	p.save()
	return render(request, 'me/index.html')

def about(request):
	p = PageView()
	p.page = "about"
	p.save()
	return render(request, 'me/about.html')

def career(request):
	# p = PageView()
	# p.page = "career"
	# p.save()
	all_exp = Experience.objects.all()
	return render(request, 'me/career.html', {'all_exp':all_exp})

def projects(request):
	# p = PageView()
	# p.page = "projects"
	# p.save()
	all_projects = project.objects.all()
	return render(request, 'me/projects.html', {"all_project":all_projects})

def education(request):
	# p = PageView()
	# p.page = "education"
	# p.save()
	return render(request, 'me/education.html')

def contact(request):
	# p = PageView()
	# p.page = "education"
	# p.save()
	# print(request.POST)
	form = MessageForm(request.POST or None)
	if form.is_valid():
		form.save()
		# print(form.cleaned_data)
		form = MessageForm()
	else:		
		form = MessageForm()	
	# form = ContactForm(request.POST or None)	
		
	context = {'form' : form}
	return render(request, 'me/contact.html', context)