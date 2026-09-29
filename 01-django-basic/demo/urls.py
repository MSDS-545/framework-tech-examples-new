"""Application-level routes map URL patterns to view functions."""
from django.urls import path
from . import views
urlpatterns = [
    # Visiting / calls the home() function in views.py.
    path("", views.home, name="home"),
]
