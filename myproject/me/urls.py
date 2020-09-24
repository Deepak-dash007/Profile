from django.urls import path, re_path
from . import views
urlpatterns = [
	path('',views.about, name='index'),
	re_path(r'about.*', views.about, name='about'),
	re_path(r'career.*', views.career, name='career'),
	re_path(r'projects.*', views.projects, name='projects'),
	re_path(r'education.*', views.education, name='education'),
    re_path(r'contact.*', views.contact, name='contact'),
    re_path(r'.*',views.about, name='index'),
]