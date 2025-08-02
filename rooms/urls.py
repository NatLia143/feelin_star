from django.urls import path
from .views import RoomFormView

urlpatterns = [
    path('crear/', RoomFormView.as_view(), name = "create_room")
]
