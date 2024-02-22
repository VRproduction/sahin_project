from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name = 'home'),

    path('about/', views.AboutPageView.as_view(), name = 'about'),

    path('services/', views.ServicePageView.as_view(), name = 'services'),
    path('services/<slug:slug>/', views.ServiceDetailPageView.as_view(), name = 'service-detail'),

    path('projects/', views.ProjectPageView.as_view(), name = 'projects'),
    path('projects/<int:pk>/', views.ProjectDetailPageView.as_view(), name = 'project-detail'),

    path('news/', views.NewsPageView.as_view(), name = 'news'),
    path('news/<slug:slug>/', views.NewsDetailPageView.as_view(), name = 'news-detail'),

    path('gallery/', views.GalleryPageView.as_view(), name = 'gallery'),

    path('contact/', views.ContactPageView.as_view(), name = 'contact'),
]
