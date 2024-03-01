from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('delivery/', views.delivery, name='delivery'),
    path('t_and_c/', views.t_and_c, name='t_and_c'),
    path('privacy/', views.privacy, name='privacy'),   
]
