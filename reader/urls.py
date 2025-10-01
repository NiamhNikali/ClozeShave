from django.urls import path
from .views import index_get, reading_create, reading_get

urlpatterns = [
    path("", index_get),
    path("create", reading_create),
    path("r/<int:pk>", reading_get),
]