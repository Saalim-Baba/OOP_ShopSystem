import customer
import order
from customer import *


class Account:

    def __init__(self):
        """
        Initialisiert ein Objekt vom Typ Account mit einer leeren Kundenreferenz und einer leeren Bestellungsliste.
        """
        self._customer = None
        self._orders = []
        customer.account = self
        order.account = self

    @property
    def customer(self):
        """
        Getter-Methode für das Kundenobjekt dieses Accounts.
        :return: Das Kundenobjekt dieses Accounts.
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """
        Setter-Methode, um das Kundenobjekt dieses Accounts festzulegen.
        :param customer: Das Kundenobjekt, das diesem Account zugeordnet werden soll.
        """
        self._customer = customer

    @property
    def orders(self):
        """
        Getter-Methode für die Liste der Bestellungen dieses Accounts.
        :return: Die Liste der Bestellungen dieses Accounts.
        """
        return self._orders

    @orders.setter
    def orders(self, order):
        """
        Setter-Methode, um die Liste der Bestellungen dieses Accounts festzulegen.
        :param order: Die Liste der Bestellungen, die diesem Account zugeordnet werden soll.
        """
        self._orders = order

    def add_order(self, order1):
        """
        Fügt eine Bestellung zur Liste der Bestellungen dieses Accounts hinzu.
        :param order1: Die Bestellung, die hinzugefügt werden soll.
        """
        self._orders.append(order1)

    def to_string_orders(self):
        """
        Zeigt alle Bestellungen dieses Accounts an und ermöglicht die Auswahl einer Bestellung zur detaillierten
        Anzeige.
        """

        print("\n-------------------------------||||| BESTELLUNGEN ||||||---------------------------\n")
        for count, order in enumerate(self._orders, start=1):
            print(f"{count}. Bestellung {order._number} ")
            print("\n-------------------------------------")

        choice = input("Bestellung anschauen? Y/N")
        if choice == "Y" and len(self._orders) > 0:
            try:
                choice = int(input(f"Welche? 1 - {len(self._orders)}:  "))
                choice -= 1
                orders = self._orders[choice]
                orders.to_string()
            except (ValueError, IndexError):
                print("Fehler: Ungültige Eingabe oder Bestellung nicht gefunden!")
        else:
            print("\n----------------- WEITERLEITUNG -----------------\n")
            self.choice()

    def choice(self):
        global choice
        print("\n----------------- ||||| ACCOUNT |||||| -------------------\n")
        catalog = Catalog()
        catalog.fill_catalog()
        while True:
            try:
                if len(self._orders) == 0:
                    choice = int(input("Bestellung machen?(2)\nVerlassen? (4)\nEingabe: "))
                if len(self._orders) > 0:
                    try:
                        choice = int(input("\nBestellungen ansehen?(1)\nBestellung erstellen?(2)\nProdukt bestellen?("
                                           "3)\nEingabe:"))
                    except ValueError:
                        print("Fehler: Bitte geben Sie eine gültige Option ein.")
                        continue
                if choice not in (2, 4) and len(self._orders) == 0:
                    print("Fehler: Keine Bestellungen vorhanden.")
                    continue
                if choice == 1:
                    self.to_string_orders()
                if choice == 2:
                    order = Order(catalog, self)
                    self.add_order(order)
                    print("\n-----------------Bestellung erstellt------------------\n")
                if choice == 3:
                    try:
                        if len(self._orders) > 1:
                            use_order = int(input(f"Welche Bestellung? 1 - {len(self._orders)}:  "))
                            if len(self._orders) > use_order > 0:
                                catalog.to_string()
                                use_order -= 1
                                this_order = self._orders[use_order]
                                this_order.order_product_by_name()
                        elif len(self.orders) == 1:
                            use_order = 1
                            catalog.to_string()
                            use_order -= 1
                            this_order = self._orders[use_order]
                            this_order.order_product_by_name()
                    except ValueError:
                        print("Fehler: Ungültige Eingabe.")
            except ValueError:
                print("Fehler: Ungültige Eingabe")


if __name__ == "__main__":
    self = Account()
    self.choice()
