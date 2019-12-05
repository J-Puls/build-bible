from django.urls import path
from . import views

urlpatterns = [
    path('vehicle/', views.vehicle, name='vehicle'),
]
