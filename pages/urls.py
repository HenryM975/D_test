from django.urls import path

from . import views

urlpatterns = [
    path('', views.homePageViev, name='home')
]