from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name = 'home'),
    path('about/', views.AboutPageView.as_view(), name = 'about'),
    path('services/<int:pk>/', views.ServiceDetailPageView.as_view(), name = 'service-detail'),
]
