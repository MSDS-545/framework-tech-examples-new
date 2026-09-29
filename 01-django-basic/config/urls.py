"""Project-level URL routing: the first routing table Django checks."""
from django.contrib import admin
from django.urls import include, path
urlpatterns = [
    path("admin/", admin.site.urls),
    # Delegate the root URL to the demo application's routing table.
    path("", include("demo.urls")),
]
