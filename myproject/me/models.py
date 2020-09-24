from django.db import models
from datetime import datetime

# Create your models here.

class Experience(models.Model):
	company = models.CharField(max_length=30)
	role = models.CharField(max_length=30)
	from_date = models.DateField(default=None, blank=True, null=True)
	till_date = models.DateField(default=None, blank=True, null=True)
	info = models.CharField(max_length=1000, default='')
	location = models.CharField(max_length=20, default='Hyderabad')
	color = models.CharField(max_length=20, default='primary')

	def __str__(self):
		return self.role + "@" + self.company


class skill(models.Model):
	skill_type = models.CharField(max_length=20, blank=True,default=None)
	technology = models.CharField(max_length=200, blank=True,default=None)


class message(models.Model):
	name = models.CharField(max_length=30,verbose_name="")
	email = models.EmailField(max_length=40,verbose_name="")
	contact = models.IntegerField(max_length=15,verbose_name="")
	message = models.CharField(max_length=1000,blank=True, null=True,verbose_name="")
	date = models.DateField(default=datetime.now)


class project(models.Model):
	title = models.CharField(max_length=30)
	desc = models.CharField(max_length=100,null=True)
	likes = models.IntegerField(max_length=10, default=0)
	repo_link = models.CharField(max_length=200,default=None, blank=True, null=True)
	tech = models.CharField(max_length=200,default=None, blank=True, null=True)
	yt_link = models.CharField(max_length=200,default=None, blank=True, null=True)


class PageView(models.Model):
	page = models.CharField(max_length=10, default="neha")
	when = models.DateField(default=datetime.now)