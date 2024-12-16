from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='index'),
    path('qeydiyyat/', views.registration, name='qeydiyyat'),
    path('about/', views.about, name='qeydiyyat'),
path('', views.index, name='index'),
    path('qeydiyyat/', views.registration, name='qeydiyyat'),
    path('about/', views.about, name='qeydiyyat'),
]
