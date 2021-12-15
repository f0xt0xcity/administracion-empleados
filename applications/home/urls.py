from django.urls import path 
from .views import ListarPrueba, PruebaCreateView, PruebaListView, PruebaView, ResumeFoundationView



urlpatterns = [
    path('', PruebaView.as_view(), name = "inicio"),
    path('lista/', PruebaListView.as_view()),
    path('listaprueba/', ListarPrueba.as_view()),
    path('add/', PruebaCreateView.as_view()),
    path(
        'resume-foundation/', 
        ResumeFoundationView.as_view()),
]