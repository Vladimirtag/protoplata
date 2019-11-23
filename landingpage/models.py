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
<<<<<<< HEAD
	title = models.CharField(max_length=100)
=======
	title = models.CharField(max_length=150)
>>>>>>> 3fe9581897153708673389c7f0324e87b517eb56
	text = models.TextField()


class Join(models.Model):
	email = models.EmailField(blank = True)
	file = models.FileField(upload_to='', blank = False, 
			validators=[validators.FileExtensionValidator(
				allowed_extensions = ['conf'],
<<<<<<< HEAD
				message = 'не совсем верное расширение')])
=======
				message = 'не верное расширение')])
>>>>>>> 3fe9581897153708673389c7f0324e87b517eb56
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.email

	def get_absolute_url(self):
		return reverse('landingpage:main')