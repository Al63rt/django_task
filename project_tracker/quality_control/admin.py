from django.contrib import admin
from .models import BugReport, FeatureRequest

admin.register(FeatureRequest)
# Класс администратора для модели BugReport
@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'status', 'priority', 'created_at', 'updated_at')
    list_filter = ('status', 'project', 'task', 'priority')
    search_fields = ('title', 'description')
    list_editable = ('status',)
    readonly_fields = ('created_at', 'updated_at')

# Класс администратора для модели FeatureRequest
@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'status', 'priority', 'created_at', 'updated_at')
    list_filter = ('status', 'project', 'task', 'priority')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')