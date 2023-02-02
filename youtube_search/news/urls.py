from django.urls import path, include, re_path

from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news_detail'),
    path('<slug:slug>/update', views.NewsUpdateView.as_view(), name='news-up'),
    path('<slug:slug>/delete', views.NewsDeleteView.as_view(), name='news-delete'),
    path('api/v1/newslist/', views.ApiNewsCreate.as_view(), name='api-create'),
    path('api/v1/newslist/<slug:slug>/', views.ApiNewsUpdate.as_view(), name='api-update'),
    path('api/v1/newslist/delete/<slug:slug>/', views.ApiNewsDelete.as_view(), name='api-delete'),
    path('api/v1/drf_sess/', include('rest_framework.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
