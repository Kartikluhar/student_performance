from django.urls import path
from . import views

urlpatterns = [
    path("", views.upload_csv, name='upload_csv'),
    path("predict/", views.predict_performance, name='predict_performance'),
    path('dashboard/', views.dashboard, name='dashboard')
]