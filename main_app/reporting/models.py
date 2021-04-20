from django.db import models

# Create your models here.
class selling_report(models.Model):
    seller_phone_number = models.IntegerField()
    buyer_phone_number = models.IntegerField()
    product_id = models.IntegerField()
    selling_price = models.DecimalField(max_digits=20, decimal_places=4)
    profit_price = models.DecimalField(max_digits=20, decimal_places=4)
    selling_date = models.DateField( auto_now_add=True)
    def __str__(self):
        return str(self.selling_date)

    def get_absolute_url(self):
        return reverse("selling_report", kwargs={"pk": self.pk})