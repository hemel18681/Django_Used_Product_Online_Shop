from django.db import models
from django.contrib.auth.models import User

class user_info(models.Model):
    user_name = models.CharField(max_length=50)
    user_mail = models.CharField(max_length=50)
    user_password = models.CharField(max_length=50)
    user_picture = models.URLField(max_length=200,blank=True, null=True)
    user_phone_number =  models.IntegerField(primary_key = True)
    def __str__(self):
        return self.user_name

    def get_absolute_url(self):
        return reverse("user_info_detail", kwargs={"pk": self.pk})
