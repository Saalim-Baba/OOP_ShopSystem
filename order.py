
from product import Product
from catalog import Catalog
import random

class Order:
    '''
    maximal 10 Produkte
    '''

    def __init__(self, catalog, account):
        """
        Initialisiert ein Objekt vom Typ Order mit einer leeren Produktliste, einer zufällig generierten Bestellnummer,
        einem Katalog und einem Kundenkonto.
        :param catalog: Der Katalog, aus dem Produkte bestellt werden können.
        :param account: Das Kundenkonto, dem diese Bestellung zugeordnet ist.
        """
        self._products = []
        self._number = random.randint(1, 100000)
        self._catalog = catalog
        self._account = account

    @property
    def cat(self):
        """
        Getter-Methode für den Katalog dieser Bestellung.
        :return: Der Katalog dieser Bestellung.
        """
        return self._catalog

    @cat.setter
    def cat(self, cat):
        """
        Setter-Methode, um den Katalog dieser Bestellung festzulegen.
        :param cat: Der Katalog, der dieser Bestellung zugeordnet werden soll.
        """
        self._catalog = cat

    @property
    def get_products(self):
        """
        Getter-Methode für die Liste der Produkte in dieser Bestellung.
        :return: Die Liste der Produkte in dieser Bestellung.
        """
        return self._products

    @property
    def account(self):
        """
        Getter-Methode für das Kundenkonto, dem diese Bestellung zugeordnet ist.
        :return: Das Kundenkonto dieser Bestellung.
        """
        return self._account

    @property
    def get_number(self):
        """
        Getter-Methode für die Bestellnummer dieser Bestellung.
        :return: Die Bestellnummer dieser Bestellung.
        """
        return self._number

    @property
    def size(self):
        """
        Getter-Methode für die Anzahl der Produkte in dieser Bestellung.
        :return: Die Anzahl der Produkte in dieser Bestellung.
        """
        return len(self._products)

    def get_value(self, i):
        """
        Getter-Methode, um den Namen des Produkts an einer bestimmten Position in der Bestellung abzurufen.
        :param i: Die Position des Produkts in der Bestellung.
        :return: Der Name des Produkts an der angegebenen Position oder None, falls die Position ungültig ist.
        """
        try:
            return self._products[i].name
        except:
            return None

    def order_product_by_name(self):
        """
        Bestellt ein Produkt aus dem Katalog basierend auf seinem Namen und der angegebenen Menge.
        Fügt das bestellte Produkt zur Liste der Produkte in dieser Bestellung hinzu.
        :param name: Der Name des zu bestellenden Produkts.
        :param amount: Die Menge des zu bestellenden Produkts.
        """
        global amount
        name = input("Name des Produkts: ")
        amount = int(input("Menge:  "))
        print("\n------------Wird überprüft--------------\n")

        product1 = self._catalog.order_product_by_name(name, amount)
        if product1 is None:
            print("Das Produkt gibt es nicht oder nicht genügend im Lager")
            return None
        else:
            self._products.append(product1)
            print(f"{product1.name} wurde bestellt für Bestellung {self._number}\n Menge: {amount}\n")

    def get_price(self, i):
        """
        Getter-Methode, um den Preis des Produkts an einer bestimmten Position in der Bestellung abzurufen.
        :param i: Die Position des Produkts in der Bestellung.
        :return: Der Preis des Produkts an der angegebenen Position oder None, falls die Position ungültig ist.
        """
        try:
            return self._products[i].price
        except:
            return None

    def to_string(self):
        """
        Gibt eine formatierte Darstellung der Produkte in dieser Bestellung aus.
        """
        print("\n------------------||||| DEIN WARENKORB ||||||---------------------\n")
        if len(self._products) == 0:
            print("\t\n--------------Noch keine Produkte-------------\n")
        for count, product in enumerate(self._products, start=1):
            print(f"{count}. Produkt: {product.name}\n Preis: {product.price} CHF\n Menge: {amount}")
            print("----------------------------------")
        print("\n")




