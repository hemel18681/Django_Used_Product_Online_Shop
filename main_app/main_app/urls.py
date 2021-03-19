from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home_page'),
    path('login/',include('authenticate.urls')),
    path('post_info/',include('post_details.urls')),
    path('admin_page/', views.admin_page, name='admin_page'),
    path('post/<int:post_id>/',views.post_view,name='post_details'),
    path('post_image/<int:post_id>/',views.indivisual_view_pic,name='indivisual_view'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
