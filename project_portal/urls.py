from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.project_submission, name='project_submission'),
    path('search/', views.project_search, name='search'),
    path('', views.home_view, name='home'),
    path('project/<int:project_id>/', views.project_detail_view, name='project_detail'),

]
