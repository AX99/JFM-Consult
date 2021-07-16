from django.urls import path
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('', views.IndexView.as_view()),
    path('about/', views.AboutView.as_view()),
    path('coaching/', views.CoachingView.as_view()),
    path('blog/', views.BlogView.as_view()),
    path('contact/', views.contact, name='contact',),
]
