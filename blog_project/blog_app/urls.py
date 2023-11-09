from . import views

from django.urls import path

from .views import addBlog, likeBlog

urlpatterns = [

    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('add/',addBlog,name='addblog'),
    path('like/<str:pk>',likeBlog,name='like'),
    path('loginpage/',views.loginpage,name='loginpage'),
    path('signup/',views.signup,name='signup'),
    path('logout',views.logout,name='logout'),


]
