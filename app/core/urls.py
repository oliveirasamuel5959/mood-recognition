from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
from .forms import LoginForm
from cam.views import main_view
app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('main/', main_view, name='main')
    #path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
