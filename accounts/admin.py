from django.contrib import admin
from .models import *

@admin.register(Bimar)
class BimarAdmin(admin.ModelAdmin):
    pass

@admin.register(Nurse)
class NurseAdmin(admin.ModelAdmin):
    pass