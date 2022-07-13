from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=20, default=99.99)

    def sale_price(self):
        return f'{float(self.price*0.8)}.2f'