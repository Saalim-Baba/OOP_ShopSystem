import pytest
from account import Account
from customer import Customer
from order import Order
from catalog import *
class TestCustomer:

    @pytest.fixture
    def customer(self):
        return Customer("john_doe", 30)

    @pytest.fixture
    def catalog(self):
        return Catalog()

    def test_username(self, customer):
        assert customer.username == "john_doe"

    def test_age(self, customer):
        assert customer.age == 30

    def test_account(self, customer):
        assert customer.account is None

    def test_set_account(self, customer):
        account_obj = Account()
        customer.account = account_obj
        assert customer.account == account_obj

    def test_order(self, customer):
        assert customer.order is None

    def test_set_order(self, customer, catalog):
        order_obj = Order(catalog)
        customer.order = order_obj
        assert customer.order == order_obj

    def test_set_account_and_order(self, customer, catalog):
        account_obj = Account()
        order_obj = Order(catalog)
        customer.account = account_obj
        customer.order = order_obj

        assert customer.account == account_obj
        assert customer.order == order_obj

if __name__ == '__main__':
    pytest.main()
