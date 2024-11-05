from django.contrib import admin
from django.urls import include, path
from app.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('app.urls')),
]
