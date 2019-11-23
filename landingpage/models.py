from django.db import models
from django.core import validators
# Create your models here.
from django.urls import reverse
from django.shortcuts import redirect


class Service(models.Model):
	title = models.CharField(max_length=150, blank=True)
	text=models.TextField()

	def __str__(self):
		return self.title	

class Manufacture(models.Model):
	title = models.CharField(max_length=150)
	text = models.TextField()


class Join(models.Model):
	email = models.EmailField(blank = True)
	file = models.FileField(upload_to='', blank = False, 
			validators=[validators.FileExtensionValidator(
				allowed_extensions = ['conf'],
				message = 'не верное расширение')])
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.email

	def get_absolute_url(self):
		return reverse('landingpage:main')