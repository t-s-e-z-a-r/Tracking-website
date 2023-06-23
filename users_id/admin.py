from django.contrib import admin
from .models import User_Url, Url

class UrlInline(admin.TabularInline):
    model = Url

class User_UrlAdmin(admin.ModelAdmin):
    inlines = [UrlInline]

admin.site.register(User_Url, User_UrlAdmin)

