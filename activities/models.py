from django.db import models


class Activity(models.Model):
    activity_name = models.CharField(max_length=200)
    is_cardio = models.BooleanField(blank=False)
    is_strength = models.BooleanField(blank=False)
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.activity_name


# class ActivityStats(models.Model):
#     activity_meta = models.ForeignKey(ActivityMeta, on_delete=models.CASCADE)
#     entry_name = models.CharField(max_length=200, default="Unnamed Activity")
#     entry_comment = models.CharField(max_length=200, blank=True)
#     start_time = models.DateTimeField()
#     end_time = models.DateTimeField()
#     percieved_difficulty = models.IntegerField()
#     percieved_performance = models.IntegerField()

#     def __str__(self):
#         return self.entry_name

#     def calculate_duration(self):
#         return (self.end_time - self.start_time) / 60
