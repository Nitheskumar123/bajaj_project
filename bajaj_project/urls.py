from django.contrib import admin
from django.urls import path
from myapp.views import bfhl, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),          # home page
    path('bfhl', bfhl, name='bfhl'),      # API page
]
