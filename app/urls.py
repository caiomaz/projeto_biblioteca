from django.urls import include, path
from app.views import *

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
]
