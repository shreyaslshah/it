from django.urls import path
from . import views

urlpatterns = [
    path('newpost/', views.new_post),
    path('create/', views.create),
    path('q1_1/', views.q1_1),
    path('q1_2/', views.q1_2),
    path('q2_1/', views.q2_1),
    path('q2_2/', views.q2_2),
    path('q2_3/', views.q2_3),
    path('q3_1/', views.q3_1),
    path('q3_2/', views.q3_2),
    path('q3_3/', views.q3_3),
    path('q4_1/', views.q4_1),
    path('q4_2/', views.q4_2),

]