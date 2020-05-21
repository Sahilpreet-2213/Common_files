# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home',views.index,name='index'),
    path('img_submition',views.img_submition,name='img_submition'),
    path('sign_in',views.sign_in,name='sign_in'),
    path('message',views.message,name='message'),
    path('images',views.images,name='images')
] 