from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import menu

urlpatterns = [
    path('menu/', menu, name='menu'),
    # Ajoutez d'autres URL pour d'autres vues si nécessaire
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
