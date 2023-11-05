from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('success/', views.registration_success, name='success_url'),
    path('check-status/', views.check_approval_status, name='check-status'),
]
