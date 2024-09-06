from django.contrib import admin
from .models import *

@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    pass

@admin.register(Service)
class CatAdmin(admin.ModelAdmin):
    pass