from django.urls import path
from . import views

urlpatterns = [
    path('update_choices/', views.update_choices, name='update_choices'),
    path('update_content/', views.update_content, name='update_content'),
]
