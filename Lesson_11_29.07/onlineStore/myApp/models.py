from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    volume_range = models.CharField(max_length=50)
    glossy_price = models.IntegerField()
    matte_price = models.IntegerField()

    def __str__(self):
        return f"{self.product.name} - {self.volume_range}"
