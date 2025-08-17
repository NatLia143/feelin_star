from django.urls import path
from . import views

app_name = "rooms"

urlpatterns = [
    path("crear/", views.create_room, name="create_room"),
]