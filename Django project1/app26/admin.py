from django.contrib import admin

# Register your models here.
from app26.models import Student
class A (admin.ModelAdmin):
	list_display=['sno','sname','ssalary','saddress']
admin.site.register(Student,A)