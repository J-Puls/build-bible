from django.urls import path
from . import views
from .views import PostDetailView, SearchListView


urlpatterns = [
    path('', views.home, name='content-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('search/', SearchListView.as_view(), name='search-results'),
    path('general_knowledge/', views.general_knowledge, name='content-general'),
    path('faq/', views.faq, name='content-faq'),
    path('community/', views.community, name='content-community'),
    path('privacy_policy/', views.privacy_policy, name='content-privacy'),
    path('cookie_policy/', views.cookie_policy, name='content-cookie'),
]