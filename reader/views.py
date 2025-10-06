from typing import Any
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from django.views.generic import CreateView, DetailView

from .models import Reading

# Create your views here.
# Let's start with a function-based view cuz it's simpler.
def index_get(request):
    return render(request, "reader/index.html", {})

class ReadingDetailView(DetailView):
    model = Reading

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        return super().get_context_data(**kwargs)

class ReadingCreateView(CreateView):
    model = Reading
    fields = '__all__'