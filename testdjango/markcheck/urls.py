from django.urls import path
from . import views

urlpatterns=[
    path("", views.home, name= "home"),
    path("alevel/", views.alevel, name= "alevel"),
    path("olevel/", views.olevel, name="olevel"),
    path("sat/", views.sat, name="sat"),
]