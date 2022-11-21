from django.urls import path
from . import views

urlpatterns = [
    path("", views.see_all_rooms),
    path("<int:room_pk>", views.see_one_rooms),
    path("<str:room_name>", views.see_one_rooms),
]