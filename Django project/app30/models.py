from django.db import models
class Office(models.Model):
	no=models.IntegerField()
	name=models.CharField(max_length=64)
	mobile=models.IntegerField()
	city=models.CharField(max_length=64)
	course=models.CharField(max_length=64)