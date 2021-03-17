from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home_page'),
    path('login/',include('authenticate.urls')),
    path('post_info/',include('post_details.urls'))
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
