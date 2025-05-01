from django.db import models


class Activity(models.Model):
    activity_name = models.CharField(max_length=200)
    is_cardio = models.BooleanField(blank=False)
    is_strength = models.BooleanField(blank=False)
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.activity_name
