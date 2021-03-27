from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#student class with name,rollnumber,department,hostel
class student(models.Model):
	name = models.CharField(max_length=200, null=True)# name
	roll = models.CharField(max_length=200, null=True)# roll number
	dept = models.CharField(max_length=200, null=True) #department
	hstl = models.CharField(max_length=200, null=True) # hostel

	def __str__(self):
		return self.name

	def ro(self):
		return self.roll

	def de(self):
		return self.dept

	def ho(self):
		return self.hstl



