"""buildbible URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views as main_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('content.urls')),
    path('', include('users.urls')),
    path('', include('vehicles.urls')),
    path('utils/', include('utils.urls')),
    path('summernote/', include('django_summernote.urls')),
] 

# handler404 = 'buildbible.views.custom_page_not_found_view'
# handler500 = 'buildbible.views.custom_error_view'
# handler403 = 'buildbible.views.custom_permission_denied_view'
# handler400 = 'buildbible.views.custom_bad_request_view'

urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)