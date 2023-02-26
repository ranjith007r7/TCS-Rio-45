from django.contrib import admin
from app30.models import Office
class OfficeAdmin(admin.ModelAdmin):
	list_display=['no','name','mobile','city','course']
admin.site.register(Office,OfficeAdmin)
