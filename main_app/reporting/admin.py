from django.contrib import admin

from .models import selling_report

class show_on_admin(admin.ModelAdmin):
    readonly_fields = ('seller_phone_number','buyer_phone_number','selling_price','profit_price','selling_date','product_id')
    list_display = ('selling_date','product_id', 'profit_price','buyer_phone_number')
    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True


admin.site.register(selling_report,show_on_admin,)