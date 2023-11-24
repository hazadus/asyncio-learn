from django.urls import path

from . import views

app_name = "async_api"

urlpatterns = [
    path("", views.requests_view, name="requests"),
]
