from django.urls import path
from . import views

urlpatterns = [
    path('',views.auth_login,name='login_page'),
    path('registration',views.auth_registration,name='registration_page'),
]
