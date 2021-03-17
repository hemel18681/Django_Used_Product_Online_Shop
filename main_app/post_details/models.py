from django.db import models
from authenticate.models import user_info
# Create your models here.

class pending_post(models.Model):
    user_phone_number = models.IntegerField()
    post_title = models.CharField(max_length=100)
    post_description = models.TextField()
    post_picture = models.ImageField(upload_to='post_images/')
    post_bkash = models.CharField(max_length=50)
    post_accept = models.BooleanField(default=False)
    def __str__(self):
        return self.post_title

    def get_absolute_url(self):
        return reverse("pending_post_detail", kwargs={"pk": self.pk})
