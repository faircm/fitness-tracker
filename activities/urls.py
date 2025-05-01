from django.urls import path
from . import views

app_name = "activities"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/usage", views.DetailView.as_view(), name="usage"),
    path("<int:activity_id>/record", views.record, name="record"),
]
