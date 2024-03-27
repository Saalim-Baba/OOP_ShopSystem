# product.py
from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    quantity: int

    def __init__(self, name, price, quantity):
        if not isinstance(name, str):
            self._name = None
        else:
            self._name = name
        self._price = price
        self._quantity = quantity

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def quantity(self):
        return self._quantity

    def decrease_quantity(self, amount):
        if amount > 0:
            if self._quantity > 0:
                self._quantity -= amount


