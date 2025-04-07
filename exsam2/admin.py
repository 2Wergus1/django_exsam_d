from django.contrib import admin
from .models import TexnikShart

@admin.register(TexnikShart)
class TexnikShartAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
