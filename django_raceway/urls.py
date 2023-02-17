from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from django.views.defaults import page_not_found


urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('trackdays/', include('trackdays.urls')),
    path('cars/', include('cars.urls')),
    path('profile/', include('profiles.urls')),
    path('checkout/', include('checkout.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'home.views.page_not_found'
