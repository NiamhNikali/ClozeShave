from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from ClozeShave.reader.models import Reading

# Create your views here.
# Let's start with a function-based view cuz it's simpler.
def index_get(request):
    return render(request, "reader/index.html", {})

@csrf_protect
def reading_create(request: HttpRequest) -> HttpResponse:
    new_reading = Reading()
    new_reading.original_text = request.POST['text_to_learn']
    new_reading.save()
    return render(request, "reader/reading.html", request.POST)