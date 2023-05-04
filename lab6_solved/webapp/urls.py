from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    path('home/', views.home_view),
    path('smartphone/', views.smartphone_view),
    path('geeks/', views.geeks_view),
    path('loggedin/', views.loggedin_view),
    path('login/', views.login_view),
    path('sesslogin/', views.sesslogin_view),
    path('sessloggedin/', views.sessloggedin_view),
    path('sesslogout/', views.sesslogout_view)
]
