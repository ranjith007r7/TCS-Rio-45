from django.db import models

class Student(models.Model):
	sno=models.IntegerField()
	sname=models.CharField(max_length=64)
	ssalary=models.FloatField()
	saddress=models.CharField(max_length=64)
