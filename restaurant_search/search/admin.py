from django.contrib import admin

# Register your models here.
# search/admin.py

from django.contrib import admin
from .models import Dish

@admin.register(Dish)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'items','full_details')
    search_fields = ('name', 'items')
