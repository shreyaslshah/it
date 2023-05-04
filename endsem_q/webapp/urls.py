from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('home/', views.homeview),
    path('submitcr/', views.submitcr),
    path('submitvote/', views.submitvote),
]