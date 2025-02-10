from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    # Other paths
    path('', TemplateView.as_view(template_name='home/main.html')),  # Home page
]
