from django.contrib import admin

# Register your models here.
from .models import pending_post

class show_on_admin(admin.ModelAdmin):
    readonly_fields = ('user_phone_number','post_title','post_description','post_picture','thumbnail_preview','post_bkash','post_given_date')
    list_display = ('post_title', 'thumbnail_preview')
    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True

admin.site.register(pending_post,show_on_admin,)
