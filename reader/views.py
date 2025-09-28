from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, request
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

# Create your views here.
# Let's start with a function-based view cuz it's simpler.
def index_get(request):
    context = {}
    return render(request, "reader/index.html", context)

@csrf_protect
def reading_create(request: HttpRequest) -> HttpResponse:
    request
    
    return HttpResponseNotFound()