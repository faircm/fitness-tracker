from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import Activity


class IndexView(generic.ListView):
    template_name = "activities/index.html"
    context_object_name = "activities_list"

    def get_queryset(self):
        return Activity.objects.order_by("-is_cardio", "activity_name")


class DetailView(generic.DetailView):
    model = Activity
    template_name = "activities/detail.html"


class UsageView(generic.DetailView):
    model = Activity
    template_name = "activities/detail.html"


def record(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)

    return HttpResponse(f"Recording entry with activity type {activity_id}")
