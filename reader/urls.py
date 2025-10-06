from django.urls import path
from .views import index_get, ReadingDetailView, ReadingCreateView

urlpatterns = [
    path("create", ReadingCreateView.as_view(), name="reading_create"),
    path("detail/<int:pk>/", ReadingDetailView.as_view(), name="reading_detail"),
]