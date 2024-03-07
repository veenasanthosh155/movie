"""
URL configuration for movie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin







from django.urls import path
from app import views
app_name="app"


urlpatterns = [

    # path('',views.home,name="home"),
    path('',views.MovieList.as_view(),name="home"),
    # path('addmovie/', views.addmovie, name="addmovie"),
    path('addmovie',views.Movieadd.as_view(),name="addmovie"),
    # path('movie/<int:p>/view/', views.viewmovie, name='viewmovie'),
    path('movie/<int:pk>',views.MovieDetail.as_view(),name="viewmovie"),
    # path('movie/<int:p>/update/', views.update, name='movieupdate'),
path('update/<int:pk>/', views.Movieupdate.as_view(), name='movieupdate'),
    # path('movie/<int:p>/deletemovie/', views.deletemovie, name='deletemovie'),
path('delete/<int:pk>/', views.Moviedelete.as_view(), name='deletemovie'),

]
