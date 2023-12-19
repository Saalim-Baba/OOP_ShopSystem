
from product import *

class Catalog:

    def __init__(self):
        """
        Initialisiert ein Objekt vom Typ Catalog mit einer leeren Katalogliste.
        """
        self._catalog = []

    @property
    def catalog(self):
        """
        Getter-Methode für die Katalogliste dieses Catalog-Objekts.
        :return: Die Katalogliste dieses Catalog-Objekts.
        """
        return self._catalog

    @catalog.setter
    def catalog(self, value):
        """
        Setter-Methode, um die Katalogliste dieses Catalog-Objekts festzulegen.
        :param value: Die Katalogliste, die diesem Catalog-Objekt zugewiesen werden soll.
        """
        self._catalog = value

    def add_product(self, product):
        """
        Fügt ein Produkt zur Katalogliste hinzu, sofern es nicht bereits im Katalog existiert.
        :param product: Das hinzuzufügende Produkt.
        """
        if product in self._catalog:
            print("Das Produkt ist bereits im Katalog.")
        else:
            self._catalog.append(product)

    def order_product_by_name(self, name, amount):
        """
        Bestellt ein Produkt aus dem Katalog basierend auf seinem Namen und der angegebenen Menge.
        Verringert die Menge des Produkts im Katalog entsprechend der Bestellung.
        :param name: Der Name des zu bestellenden Produkts.
        :param amount: Die Menge des zu bestellenden Produkts.
        :return: Das bestellte Produkt oder None, wenn das Produkt nicht gefunden wurde.
        """
        global product1
        for product1 in self._catalog:  # Verwenden Sie hier self._catalog
            if product1.name == name:
                quantity = self.remove_quantity_by_amount(product1.name, amount)  # Verwenden Sie self.remove_quantity_by_amoun# t
                if quantity == amount:
                    return product1
                else:
                    return None
        return None

    def remove_quantity_by_amount(self, name, amount):
        """
        Verringert die Menge eines Produkts im Katalog um die angegebene Menge.
        :param name: Der Name des zu aktualisierenden Produkts.
        :param amount: Die Menge, um die die Produktmenge verringert werden soll.
        :return: Die tatsächlich reduzierte Menge oder "Nicht genug im Lager" bzw. "Produkt nicht gefunden".
        """
        for i in self._catalog:  # Verwenden Sie hier self._catalog
            if i.name == name:
                if amount <= i.quantity:
                    i.decrease_quantity(amount)
                    return amount
                else:
                    return "Nicht genug im Lager"
        return "Produkt nicht gefunden"

    def to_string(self):
        """
        Gibt eine formatierte Darstellung des Katalogs aus.
        """
        print("\n")
        print("\t||||| WILLKOMMEN ZU UNSEREM KATALOG ||||||\n ------------------------------------------------")
        for count, product in enumerate(self._catalog, start=1):
            print(f"{count}. Produkt: {product.name}\n Preis:{product.price} CHF\n Menge:{product.quantity}")
            print("---")
        print("\n")

    def fill_catalog(self):
        product1 = Product("Panzerfaust", 23, 3)
        product2 = Product("Schrauben", 10, 100)
        product3 = Product("Hammer", 30, 2)
        product4 = Product("Nägel", 5, 100)
        product5 = Product("Schraubendreher", 15, 7)
        product6 = Product("Zange", 20, 4)
        product7 = Product("Säge", 40, 5)
        product8 = Product("Schraubenschlüssel", 18, 6)
        product9 = Product("Bohrmaschine", 70, 3)
        product10 = Product("Wasserwaage", 25, 5)
        product11 = Product("Messer", 12, 10)
        product12 = Product("Schleifmaschine", 55, 2)
        product13 = Product("Sicherheitsbrille", 8, 15)
        product14 = Product("Steckschlüsselsatz", 28, 4)
        product15 = Product("Maulschlüssel", 15, 7)
        product16 = Product("Stechbeitel", 14, 8)
        product17 = Product("Schraubzwinge", 32, 3)
        product18 = Product("Tischkreissäge", 120, 1)
        product19 = Product("Kreuzschlitzschraubendreher", 8, 12)
        product20 = Product("Winkelschleifer", 45, 5)


        self.add_product(product1)
        self.add_product(product2)
        self.add_product(product3)
        self.add_product(product4)
        self.add_product(product5)
        self.add_product(product6)
        self.add_product(product7)
        self.add_product(product8)
        self.add_product(product9)
        self.add_product(product10)
        self.add_product(product11)
        self.add_product(product12)
        self.add_product(product13)
        self.add_product(product14)
        self.add_product(product15)
        self.add_product(product16)
        self.add_product(product17)
        self.add_product(product18)
        self.add_product(product19)
        self.add_product(product20)




