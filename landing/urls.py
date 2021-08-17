from django.urls import path
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('coaching/', views.CoachingView.as_view(), name='coaching'),
    # path('blog/', views.BlogView.as_view(), name='blog'),
    path('contact/', views.contact, name='contact',),
]
