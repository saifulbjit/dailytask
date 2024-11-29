from django.urls import path, include
from . import views

app_name = 'jobs'

urlpatterns = [
    path('', views.Homepage.as_view(), name='homepage'),
    path('api/', include('jobs.api.urls')),
    path('category/create/', views.category_create_view, name='category_create'),
    path('job/add/', views.job_add_view, name='add_job'),
    path('job/<int:pk>/', views.view_job_detail, name='view_job'),
    path('job/<int:pk>/apply/', views.apply_for_job, name='apply_job'),
]
