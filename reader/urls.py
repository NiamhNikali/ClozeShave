from django.urls import include, path
from .views import index_get

urlpatterns = [
    path("index.html", index_get),
]