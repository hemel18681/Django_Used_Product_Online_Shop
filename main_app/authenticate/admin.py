from django.contrib import admin

from .models import user_info


class show_on_admin(admin.ModelAdmin):
    readonly_fields = ('user_join_date','user_name','user_mail','user_password','user_picture','thumbnail_preview','user_phone_number',)
    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True

admin.site.register(user_info,show_on_admin,)