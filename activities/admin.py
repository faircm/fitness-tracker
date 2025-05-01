from django.contrib import admin
from .models import Activity


class ActivityAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Activity Information", {"fields": ["activity_name", "description"]}),
        ("Activity Type", {"fields": ["is_cardio", "is_strength"]}),
    ]


admin.site.register(Activity, ActivityAdmin)
# Register your models here.
