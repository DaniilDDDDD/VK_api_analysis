from django.urls import path

from . import views

urlpatterns = [
    path('wall/<str:plot_type>/', views.wall, name='wall'),
    path('stats/<str:plot_type>/', views.stats, name='stats'),
    path('tag/', views.tag, name='tag'),
]
