from django.urls import path
from django.views.generic.base import TemplateView
from .import views

urlpatterns = [
    path('', views.index),
    path('<str:sublink>', views.result),

    path(r'^bgpage/', TemplateView.as_view(template_name="bgtemplate.html"),
                   name='page_bg'),
    path(r'^colorpage/', TemplateView.as_view(template_name="colortemplate.html"),
                   name='page_color'),
    path(r'^404page/', TemplateView.as_view(template_name="404.html"),
                   name='page_404'),

]