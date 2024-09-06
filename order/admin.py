from django.contrib import admin
from .models import *
@admin.register(Orders)
class ModelNameAdmin(admin.ModelAdmin):
    pass