from django.contrib import admin

from .models import selling_report

class show_on_admin(admin.ModelAdmin):
    readonly_fields = ('user_phone_number','post_title','post_description','post_picture','thumbnail_preview','post_money','post_used_days','post_given_date')
    


admin.site.register(selling_report,)