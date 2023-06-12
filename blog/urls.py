
from django.contrib import admin
from django.urls import path
from contentwork.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home),
    path("insert/", insert),
]
