from django.contrib import admin

# Register your models here.
from .models import Join, Service, Manufacture

class ServiceAdmin(admin.ModelAdmin):
	list_display = 	['title', 'text']

	list_display_links = None

	list_editable = ['title', 'text']
	

class ManufactureAdmin(admin.ModelAdmin):
	list_display=['title', 'text']

class JoinAdmin(admin.ModelAdmin):
	list_display=['email', 'file']


admin.site.register(Manufacture, ManufactureAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Join, JoinAdmin)