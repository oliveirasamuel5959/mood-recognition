from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'cam'

urlpatterns = [
    path('main', views.main_view, name='main'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
