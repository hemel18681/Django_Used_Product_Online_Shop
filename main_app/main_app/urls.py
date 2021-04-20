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
    path('payment/<int:post_id>/',views.complete_payment_work,name='complete_payment'),
    path('order_done/',views.make_report,name='generate_report'),
    path('thank-you/',views.thankyou,name='thank_you'),
    path('report/',include('reporting.urls')),
    path('search/<str:search_name>',views.search_product,name='search_result')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
