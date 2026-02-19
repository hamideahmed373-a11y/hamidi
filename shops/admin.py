from django.contrib import admin
from .models import *
class BaseAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Base,BaseAdmin)
admin.site.register(Offers)
admin.site.register(How)
# Register your models here.