from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/', dashboard_view, name='dashboard'),
    path('calendar/', calendar_view, name='calendar'),
    path('employees/', employees_view, name='employees'),
]

