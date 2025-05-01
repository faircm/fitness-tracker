from django.contrib import admin
from .models import Activity, Workout


class ActivityInline(admin.StackedInline):
    model = Activity


class WorkoutAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Workout Information", {"fields": ["workout_name", "workout_activity"]}),
        ("Date/Time", {"fields": ["start_time", "end_time"]}),
        ("Additional Data", {"fields": ["effort", "performance", "comments"]}),
    ]


admin.site.register(Workout, WorkoutAdmin)
