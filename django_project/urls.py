 # django_project/urls.py
from django.contrib import admin
from django.urls import path, include
 
 
 
 # new
urlpatterns = [
path("admin/", admin.site.urls),
path("", include("pages.urls")), 
# User management
path("accounts/", include("django.contrib.auth.urls")),
# Local apps
path("accounts/", include("accounts.urls")), # new
path("", include("pages.urls")),
]