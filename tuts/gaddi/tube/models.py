from django.db import models

# Create your models here.
class Employee(models.Model):
	firstname= models.CharField(max_length= 200)
	lastname = models.CharField(max_length= 200)
	emp_id = models.IntegerField()
	workinghours = models.IntegerField()
	experience = models.IntegerField(default=2)
	name = models.CharField(max_length= 100, default= '')
	def __str__(self):
		return self.firstname

