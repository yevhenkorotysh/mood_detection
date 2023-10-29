from django.contrib import admin
from .models import *

@admin.register(AudioFile)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = [
        'file_name',
        'duration',
        'mood_detected',
    ]

