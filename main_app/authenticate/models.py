from django.db import models

class user_info(models.Model):
    user_name = models.CharField(max_length=50)
    user_password = models.CharField(max_length=50)
    user_mail = models.CharField(max_length=50)
    user_picture = models.ImageField(blank=True, null=True, upload_to='images/')
    user_phone_number =  models.IntegerField(primary_key = True)

    def __str__(self):
        return self.user_name

    def get_absolute_url(self):
        return reverse("user_info_detail", kwargs={"pk": self.pk})
