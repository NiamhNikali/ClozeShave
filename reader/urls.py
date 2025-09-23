from django.urls import include, path
from .views import index_get, reading_create

urlpatterns = [
    path("", index_get),
    path("create", reading_create),
]