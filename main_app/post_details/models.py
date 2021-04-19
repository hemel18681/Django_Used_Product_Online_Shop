from django.db import models
from authenticate.models import user_info
from sorl.thumbnail import get_thumbnail
from django.utils.html import format_html
# Create your models here.

class pending_post(models.Model):
    user_phone_number = models.IntegerField()
    post_title = models.CharField(max_length=100)
    post_description = models.TextField()
    post_picture = models.ImageField(upload_to='post_images/')
    post_money = models.DecimalField(max_digits=20, decimal_places=2)
    post_used_days = models.IntegerField(default=0)
    post_accept = models.BooleanField(default=False)
    post_given_date = models.DateField( auto_now_add=True)
    def __str__(self):
        return self.post_title

    def get_absolute_url(self):
        return reverse("pending_post_detail", kwargs={"pk": self.pk})
    
    @property
    def thumbnail_preview(self):
        if self.post_picture:
            _thumbnail = get_thumbnail(self.post_picture,
                                   '300x300',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_thumbnail.url, _thumbnail.width, _thumbnail.height))
        return ""

class running_post(models.Model):
    user_phone_number = models.IntegerField()
    post_title = models.CharField(max_length=100)
    post_description = models.TextField()
    post_picture = models.ImageField(upload_to='post_images/')
    post_money = models.DecimalField(max_digits=20, decimal_places=2)
    post_used_days = models.IntegerField(default=0)
    done_post = models.BooleanField(default=False)
    post_given_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.post_title

    def get_absolute_url(self):
        return reverse("running_post_detail", kwargs={"pk": self.pk})
    
    @property
    def thumbnail_preview(self):
        if self.post_picture:
            _thumbnail = get_thumbnail(self.post_picture,
                                   '300x300',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_thumbnail.url, _thumbnail.width, _thumbnail.height))
        return ""



class done_post(models.Model):
    user_phone_number = models.IntegerField()
    post_title = models.CharField(max_length=100)
    post_description = models.TextField()
    post_picture = models.ImageField(upload_to='post_images/')
    post_money = models.DecimalField(max_digits=20, decimal_places=2)
    post_used_days = models.IntegerField(default=0)
    done_post = models.BooleanField(default=False)
    post_given_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.post_title

    def get_absolute_url(self):
        return reverse("done_post_detail", kwargs={"pk": self.pk})
    
    @property
    def thumbnail_preview(self):
        if self.post_picture:
            _thumbnail = get_thumbnail(self.post_picture,
                                   '300x300',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_thumbnail.url, _thumbnail.width, _thumbnail.height))
        return ""