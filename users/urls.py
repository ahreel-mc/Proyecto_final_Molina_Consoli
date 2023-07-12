"""Defines URL patterns for users"""
from django.urls import path, include
from . import views
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'users'
urlpatterns = [
    # Include default auth urls.
    path('', include('django.contrib.auth.urls')),
    # Registration page.
    path('register/', views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)