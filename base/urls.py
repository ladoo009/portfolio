from django.urls import path
from . import views



urlpatterns = [
    path('', views.home),
    path('pro/', views.pro),
    path('test/', views.test),
]


