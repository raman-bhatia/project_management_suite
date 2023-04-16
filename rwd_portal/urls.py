from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('project_portal/', include('project_portal.urls')),   
    # ... other app URLs ...
]
