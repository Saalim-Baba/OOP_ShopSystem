import pytest
# Assuming the Catalog and Product classes are defined elsewhere as mentioned.
from catalog import Catalog
from product import Product
from order import Order

class TestOrder:
    @pytest.fixture
    def catalog(self):
        catalog = Catalog()
        # Simulating adding some products to the catalog for testing.
        catalog.add_product(Product("Maserati", 13456, 5))  # Assuming Catalog has an add_product method.
        catalog.add_product(Product("Ferrari", 24567, 3))
        return catalog

    @pytest.fixture
    def account(self):
        # Assuming there's an Account class defined elsewhere.
        # This is a placeholder for an actual account object.
        return {"id": 12345, "name": "Test User"}

    @pytest.fixture
    def order(self, catalog, account):
        return Order(catalog, account)

    def test_order_initialization(self, order):
        assert order.size == 0


