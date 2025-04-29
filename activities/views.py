from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Activity


def index(request):
    activities_list = Activity.objects.order_by("activity_name")[:10]
    context = {"activities_list": activities_list}
    return render(request, "activities/index.html", context)


def detail(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)
    return render(request, "activities/detail.html", {"activity": activity})
    # try:
    #     activity = Activity.objects.get(pk=activity_id)
    # except Activity.DoesNotExist:
    #     raise Http404("Activity not found")
    # return render(request, "polls/detail.html", {"activity": activity})


def usage(request, activity_id):
    return HttpResponse(f"Listing details for activity {activity_id}")


def record(request, activity_id):
    return HttpResponse(f"Recording entry with activity type {activity_id}")
