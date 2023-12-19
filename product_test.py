# test_product.py
from product import Product

class TestProduct:

    def test_product_initial_name_okay(self):
        product = Product("Lol", 12345)
        assert product.name == "Lol"

    def test_product_initial_number_okay(self):
        product = Product("Lol", 12345.0)
        assert product.price == 12345.0

    def test_product_initial_name_notastring(self):
        product = Product(12, 12345)
        assert product.name is None


