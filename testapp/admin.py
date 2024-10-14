from django.contrib import admin
from .models import CandidateTimestamp

@admin.register(CandidateTimestamp)
class CandidateTimestampAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'value', 'year', 'month', 'day', 'created_at', 'updated_at')
    list_filter = ('year', 'month', 'day')
    search_fields = ('value', 'timestamp')
    readonly_fields = ('year', 'month', 'day', 'created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('timestamp', 'value')
        }),
        ('Auto-populated fields', {
            'fields': ('year', 'month', 'day', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def save_model(self, request, obj, form, change):
        obj.save()