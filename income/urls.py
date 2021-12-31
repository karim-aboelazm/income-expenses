from django.urls import path
from .views import *

app_name = 'income'
urlpatterns = [
    path('',HomePage.as_view(),name='home')
]
