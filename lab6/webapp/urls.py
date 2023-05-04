from django.urls import path
from . import views


urlpatterns = [
    path('hello/', views.say_hello),
    path('q1_1/', views.q1_1_view),
    path('q1_2/', views.q1_2_view),
    path('q2_1/', views.q2_1_view),
    path('q2_2/', views.q2_2_view),
    path('q3_1/', views.q3_1_view),
    path('q3_2/', views.q3_2_view),
    path('q4_1/', views.q4_1_view),
    path('q4_2/', views.q4_2_view),
]
