from django.db import models
from activities.models import Activity


class Workout(models.Model):
    workout_name = models.CharField(max_length=200)
    workout_activity = models.ForeignKey(Activity, on_delete=models.CASCADE, default=12)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    effort = models.IntegerField(default=1)
    performance = models.IntegerField(default=1)
    comments = models.CharField(max_length=500)

    def __str__(self):
        return self.workout_name
