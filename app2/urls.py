
from django.urls import path
from . import views


urlpatterns = [
    path('', views.info ,name='info page'),
    path('about1/', views.about1 ,name='about1'),
]

