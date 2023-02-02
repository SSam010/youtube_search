from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login1'),
    path('logout/', views.logout_user, name='logout1'),
    path('contacts/', views.contacts, name='contacts')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
