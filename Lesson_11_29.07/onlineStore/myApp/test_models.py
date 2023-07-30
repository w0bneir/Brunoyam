import unittest
from django.test import TestCase
from .models import Product, Price


class ProductModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Test Product",
            size="10x10",
        )

    def test_product_name(self):
        self.assertEqual(str(self.product), 'Test Product')

    def test_product_size(self):
        self.assertEqual(self.product.size, '10x10')


class PriceModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Test Product",
            size="10x10",
        )
        self.price = Price.objects.create(
            product=self.product,
            volume_range="10x10",
            glossy_price=10,
            matte_price=20
        )

    def test_price_product(self):
        self.assertEqual(self.price.product, self.product)

    def test_price_volume_range(self):
        self.assertEqual(self.price.volume_range, '10x10')

    def test_price_glossy_price(self):
        self.assertEqual(self.price.glossy_price, 10)

    def test_price_matte_price(self):
        self.assertEqual(self.price.matte_price, 20)


if __name__ == '__main__':
    unittest.main()
