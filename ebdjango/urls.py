"""URL routes for the assignment demo."""

from django.contrib import admin
from django.urls import path

from .views import home


urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
]
