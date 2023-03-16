from shoe_store.src.model.product import Product
from shoe_store.src.model.category import Category
from shoe_store.src.model.store import Store
from shoe_store.src.model.cart_item import CartItem


class Controller:
    def __init__(self):
        self._store = None
        self._cart = []
        self.initialize_store_data()

    def get_store(self):
        return self._store

    def get_cart(self):
        return self._cart

# the models of the style of shoes the user can pick from
    def initialize_store_data(self):
        all_running_shoes = [
            Product("Nike Air Max", 180),
            Product("Adidas Ultra Boost", 230),
            Product("Asics Gel Kayano", 150),
            Product("New Balance 574", 100),
            Product("Puma Clyde", 80),
            Product("Vans Old Skool", 70)
        ]
        all_sports_shoes = [
            Product("Adidas Ultra Boost", 250),
            Product("Asics Gel Kayano", 300),
            Product("New Balance 574", 150),
            Product("Puma Clyde", 120),
            Product("Vans Old Skool", 130)

        ]
        all_everyday_shoes = [
            Product("Converse Chuck Taylor All Star", 80),
            Product("Vans Classic Slip-On", 90),
            Product("Adidas Stan Smith", 100),
            Product("Reebok Classic Leather", 90),
            Product("Puma Cali", 110),
            Product("New Balance 990", 200)
        ]


        running_category = Category("Running Shoes")
        sports_category = Category("Sports Shoes")
        everyday_category = Category("Everyday Shoes")

        running_category.add_all_products(all_running_shoes)
        sports_category.add_all_products(all_sports_shoes)
        everyday_category.add_all_products(all_everyday_shoes)

        shoe_store = Store("Bailey's Shoes")
        shoe_store.add_all_categories([
            running_category,
            sports_category,
            everyday_category]
        )
        self._store = shoe_store

