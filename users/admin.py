from django.contrib import admin

# Register your models here.
from .models import userm

class modeladmin(admin.ModelAdmin):
    list_display=['f_name','l_name','email']

admin.site.register(userm,modeladmin)    