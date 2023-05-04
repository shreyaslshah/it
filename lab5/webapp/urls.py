from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    path('q1/', views.q1),
    path('q2/', views.q2),
    path('q3/', views.q3),
    path('q4/', views.q4),
]