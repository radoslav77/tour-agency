from django.contrib import admin
from django.contrib.auth.models import User

from .models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display=("id","username","email","password")

class BlogAdmin(admin.ModelAdmin):
    list_display = ("id","title","user","date","image","text","price","from_date","to_date")

admin.site.register(Blog,BlogAdmin)

class CountryAdmin(admin.ModelAdmin):
   list_display = ("id","holiday","country","categories")

admin.site.register(Country,CountryAdmin)

class ArchiveAdmin(admin.ModelAdmin):
    list_display = ("archive", "title", "date")

admin.site.register(Archive,ArchiveAdmin)
admin.site.register(Search)
admin.site.register(Booking)
admin.site.register(Checkout)