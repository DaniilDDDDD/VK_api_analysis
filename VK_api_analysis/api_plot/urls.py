from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('wall/<str:plot_type>/', views.wall, name='wall'),
    path('stats/<str:plot_type>/', views.stats, name='stats')
]
