from django.urls import path
from . import views


urlpatterns = [
    path('jobs/', views.JobListCreateView.as_view(), name='all_jobs'),
    path('jobs/<int:pk>/', views.JobDetailView.as_view(), name='job_detail'),
]
