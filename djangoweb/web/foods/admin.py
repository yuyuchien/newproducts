from django.contrib import admin

# Register your models here.


from .models import foodsList

admin.site.register(foodsList)