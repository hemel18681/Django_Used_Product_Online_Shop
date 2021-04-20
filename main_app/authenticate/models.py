from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import get_thumbnail
from django.utils.html import format_html

class user_info(models.Model):
    user_name = models.CharField(max_length=50)
    user_mail = models.CharField(max_length=50)
    user_password = models.CharField(max_length=50)
    user_picture = models.ImageField(upload_to='user_images/', blank=True, null=True)
    user_phone_number =  models.IntegerField(primary_key = True)
    user_join_date = models.DateField( auto_now_add=True)
    def __str__(self):
        return self.user_name

    def get_absolute_url(self):
        return reverse("user_info_detail", kwargs={"pk": self.pk})

    @property
    def thumbnail_preview(self):
        if self.user_picture:
            _thumbnail = get_thumbnail(self.user_picture,
                                   '300x300',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_thumbnail.url, _thumbnail.width, _thumbnail.height))
        return ""

