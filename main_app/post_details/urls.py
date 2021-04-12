from django.urls import path,include
from post_details import views

urlpatterns = [
    path('',views.check_post,name='wait_post'),
    path('syncronize',views.syncronize_post,name='syncronize_post'),
    path('update_post/<int:post_id>/',views.update_post,name='update_post'),
]
