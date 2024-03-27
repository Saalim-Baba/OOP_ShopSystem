import pytest
from product import Product

class TestProduct:
    @pytest.fixture
    def valid_product(self):
        return Product("Test Product", 100.0, 10)

    @pytest.fixture
    def invalid_name_product(self):
        return Product(None, 100.0, 10)

    def test_product_initialization(self, valid_product):
        assert valid_product.name == "Test Product"
        assert valid_product.price == 100.0
        assert valid_product.quantity == 10

    def test_product_initialization_with_invalid_name(self, invalid_name_product):
        assert invalid_name_product.name is None

    def test_decrease_quantity(self, valid_product):
        valid_product.decrease_quantity(3)
        assert valid_product.quantity == 7

    def test_decrease_quantity_with_invalid_amount(self, valid_product):
        valid_product.decrease_quantity(-5)
        assert valid_product.quantity == 10

    def test_decrease_quantity_below_zero(self, valid_product):
        valid_product.decrease_quantity(20)
        assert valid_product.quantity == -10

