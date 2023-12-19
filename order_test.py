import pytest
from catalog import Catalog
from product import Product
from order import  Order
# test_order.py
from order import Order  # Replace 'your_module' with the actual module containing the 'Order' class

class TestOrder:



    @pytest.fixture
    def order(self, catalog):
        return Order(12455, catalog)

    @pytest.fixture
    def catalog(self):
        return Catalog()

    def test_products_list_isempty(self, order):
        product = order
        assert len(product._products) == 0

    def test_products_list_one_item(self, order):
        order.add_products(Product("Masarati", 13456, 5))
        assert order.size == 1

    def test_products_list_two_items(self, order):
        order.add_products(Product("Masarati", 13456, 5))
        order.add_products(Product("Ferrari", 24567, 5))
        assert order.size == 2

    def test_products_list_maximum_items(self, order):
        for i in range(10):
            order.add_products(Product(f"Product {i}", i * 1000, 5))
        assert order.size == 10

    def test_products_list_more_than_maximum_items(self, order):
        for i in range(12):
            order.add_products(Product(f"Product {i}", i * 1000, 5))
        assert order.size == 10
