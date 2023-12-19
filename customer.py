from account import *

from order import *


class Customer:

    def __init__(self, username, age):
        self._username = username
        self._age = age
        self._account = None



    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, account):
        self._account = account



    def account_to_string(self):
        choice = int(input("Profil (1)\nAccount (2)\nEingabe:"))
        if choice == 1:
            change = int(input(f"\nUSERNAME:{self.username}\nALTER{self.age}\n\nDaten ändern?\nJa (1)\nNein(2)\n"))
            if change == 1:
                name = input("Do you want to change your name? Y/N")
                if name == "Y":
                    self.username = input("Enter new name: ")
                    self.account_to_string()
                else:
                    age = input("Do you want to change your age? Y/N")
                    if age == "N":
                        self.age = int(input("Enter new age"))
                        self.account_to_string()
            else:
                self.account_to_string()
        elif choice == 2:
            print(self.account.choice())
        else:
            print("Invalid Input")


if __name__ == '__main__':
    catalog = Catalog()
    account = Account()

    max_order = Order(catalog, account)
    max = Customer("maxiGHG", 12)
    lol = Product("Lol", 12, 5)
    max.account = account

    max.account_to_string()
