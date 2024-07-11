from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_update, name='add_update'),
    path('disaster/<int:disaster_id>/', views.disaster_detail, name='disaster_detail'),
]
