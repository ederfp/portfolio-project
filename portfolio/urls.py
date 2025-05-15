from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home, name='home'),
    path('projetos/', views.projects, name='projects'),
    path('projeto/<int:pk>/', views.project_detail, name='project_detail'),
    path('contato/', views.contact, name='contact'),
]