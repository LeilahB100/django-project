from django.contrib import admin

from .models import Authors


class Authoradmin(admin.ModelAdmin):
    list_display = ("name", "contact", "address", "gender")

admin.site.register(Authors, Authoradmin)
