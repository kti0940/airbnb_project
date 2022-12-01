from django.urls import path
from .views import PhotoDelete

urlpatterns = [
    path("photos/<int:pk>", PhotoDelete.as_view()),
]
