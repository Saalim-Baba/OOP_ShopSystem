from account import Account
from catalog import Catalog
from customer import Customer
from order import Order
from product import Product


def main():

    '''
    Gebe die Bestellung aus mit dem Namen des Kunden
    '''


    max = Customer("max", 12)
    account = Account()
    max.account = account
    max.account_to_string()

if __name__ == '__main__':
    main()