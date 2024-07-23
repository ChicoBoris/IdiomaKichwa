from django.urls import path

from pruebaDjango1 import settings
from .views import home

urlpatterns = [
    path('', home, name='home'),
]
if settings.DEBUG:
    urlpatterns += settings.STATIC_URL(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)