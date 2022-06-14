from re import template
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.loginuser, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('register/', views.registeruser, name='register'),
    path('', views.gallery, name='gallery'),
    path('photo/<str:pk>/', views.view, name='view'),
    path('add/', views.add, name='add'),
    path('delete_confirmation/<str:pk>/', views.delete, name='delete'),
    path('delete_cat/<str:pk>/', views.delete_cat, name='del'),
    path('del_user/<str:pk>/', views.del_user, name='del_user'),
    path('delete/<str:pk>/', views.delet, name='delet'),
    path('confirm_delete_cat/<str:pk>/', views.confirm_delete_cat, name='con_del_cat'),
    path('confirm_delete_user/<str:pk>/', views.confirm_delete_user, name='confirm_delete_user'),

    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="photos/reset_password.html"),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="photos/reset_password_sent.html") , name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="photos/reset.html"),name='password_reset_confirm'),
    path('reset_password_complete',auth_views.PasswordResetCompleteView.as_view(template_name="photos/done.html"),name='password_reset_complete'),

]
