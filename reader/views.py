from django.shortcuts import render

# Create your views here.
# Let's start with a function-based view cuz it's simpler.
def index_get(request):
    context = {}
    return render(request, "reader/index.html", context)

def reading_create(request):
    # Add the reading to the database
    # Redirect to the new reading
    return None