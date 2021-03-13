from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.auth_login,name='login_page'),
    path('registration',views.auth_registration,name='registration_page'),
    path('logout',views.auth_logout,name='logout'),
    path('resetpass',views.forget_password,name='password_reset')

]
