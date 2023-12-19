import pytest

import account
from account import Account
from order import *

class TestAccount:


    @pytest.fixture
    def order(self):
        return Order(1233)


    def test_empty_orders(self):
        assert self._orders.size == 0


    def test_account_add_order(self):
        account.add_order(Account())