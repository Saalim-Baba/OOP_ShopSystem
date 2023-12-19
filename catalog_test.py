import pytest
from product import Product  # Stellen Sie sicher, dass 'Product' korrekt importiert ist
from catalog import Catalog  # Importieren Sie die zu testende Klasse


class TestCatalog:

    def test_add_product(self):
        catalog = Catalog()
        product = Product("Test_Produkt", 23, 3)
        catalog.add_product(product)
        assert len(catalog.catalog) == 1
        assert catalog.catalog[0] == product

    def test_duplicate_product(self):
        catalog = Catalog()
        product = Product("Test_Produkt", 23, 3)
        catalog.add_product(product)
        catalog.add_product(product)  # Versuchen Sie, dasselbe Produkt erneut hinzuzufügen
        assert len(catalog.catalog) == 1  # Die Länge sollte immer noch 1 sein

    def test_order_product_by_name(self):
        catalog = Catalog()
        product = Product("Test_Produkt", 23, 3)
        catalog.add_product(product)
        ordered_product = catalog.order_product_by_name("Test_Produkt", 1)
        assert ordered_product == product  # Überprüfen Sie, ob das bestellte Produkt korrekt ist
        assert product.quantity == 2  # Überprüfen Sie, ob die Menge im Produkt aktualisiert wurde

    def test_order_nonexistent_product(self):
        catalog = Catalog()
        ordered_product = catalog.order_product_by_name("Nonexistent", 1)
        assert ordered_product is None  # Das Produkt sollte nicht gefunden werden

    def test_remove_quantity_by_amount(self):
        catalog = Catalog()
        product = Product("Test_Produkt", 23, 3)
        catalog.add_product(product)
        removed_quantity = catalog.remove_quantity_by_amount("Test_Produkt", 2)
        assert removed_quantity == 2
        assert product.quantity == 1

    def test_remove_quantity_by_amount_invalid(self):
        catalog = Catalog()
        product = Product("Test_Produkt", 23, 3)
        catalog.add_product(product)
        removed_quantity = catalog.remove_quantity_by_amount("Test_Produkt", 4)
        assert removed_quantity == "Nicht genug im Lager"
        assert product.quantity == 3


if __name__ == '__main__':
    pytest.main()
