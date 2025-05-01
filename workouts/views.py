from django.shortcuts import render
from django.views import generic
from .models import Workout


class IndexView(generic.ListView):
    template_name = "workouts/index.html"
    context_object_name = "workouts_list"

    def get_queryset(self):
        return Workout.objects.order_by("start_time")


class DetailView(generic.DetailView):
    model = Workout
    template_name = "workouts/detail.html"
