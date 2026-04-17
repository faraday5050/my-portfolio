from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('project/<slug:slug>/', views.project_detail, name='project_detail'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('send-email/', views.send_contact_email, name='send_email'),
]