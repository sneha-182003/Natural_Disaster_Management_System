# disasters/admin.py
from django.contrib import admin
from .models import DisasterUpdate

@admin.register(DisasterUpdate)
class DisasterUpdateAdmin(admin.ModelAdmin):
    list_display = ('disaster_type', 'location', 'date_reported')
    search_fields = ('disaster_type', 'location')

