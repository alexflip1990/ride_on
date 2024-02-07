from django.urls import path
from . import views

urlpatterns = [
    path('', views.announcement_list, name='announcement_list'),
    path('announcement/<int:pk>/', views.announcement_detail,
         name='announcement_detail'),
    path('announcement/new/', views.announcement_create,
         name='announcement_create'),
    path('announcement/<int:pk>/edit/',
         views.announcement_edit, name='announcement_edit'),
    path('announcement/<int:pk>/delete/',
         views.announcement_delete, name='announcement_delete'),
]
