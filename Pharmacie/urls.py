from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('', home, name='home'),

    path('', Affichage.as_view(), name='home'),
    path('ajout-donnees/', ajout_donnees, name='ajout-donnees'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)