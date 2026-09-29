"""Django views receive HTTP requests and return HTTP responses."""
from django.shortcuts import render

def home(request):
    # Context is Python data made available to the HTML template.
    context = {
        "framework": "Django",
        "message": "Hello from Django!",
    }
    # render() finds the template, inserts context data, and returns HTML.
    return render(request, "demo/home.html", context)
