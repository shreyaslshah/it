from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.hello),
    path('form/', views.formview),
    path('formsubmit/', views.formsubmit),
    path('db1/', views.db1),
    path('db2/', views.db2),
    path('dbget/', views.dbget),
    path('dbfilter/', views.dbfilter),
    path('dbupdate/', views.dbupdate),
    path('dbdelete/', views.dbdelete),

]
