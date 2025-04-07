from django.urls import path
from . import admin
from .views import home
from django.urls import path, include


urlpatterns = [
    path('', home, name='home'),
    path('user/', include('users.urls')),
]


