from django.contrib import admin
from .models import Text
# Register your models here.
class TextAdmin(admin.ModelAdmin):
	list_display=['id','topic','created_on','creator']
admin.site.register(Text,TextAdmin)