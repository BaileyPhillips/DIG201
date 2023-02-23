from shoe_store.src.model.product import Product
from shoe_store.src.model.category import Category
from shoe_store.src.model.store import Store


class Controller:
    def __init__(self):
        self._store = None
        self.initialize_store_data()

    def get_store(self):
        return self._store

    def initialize_store_data(self):
        all_running_shoes = [
            Product("Nike Air Max", 10),
            Product("Adidas Ultra Boost", 20),
            Product("Asics Gel Kayano", 30),
            Product("New Balance 574", 40),
            Product("Puma Clyde", 50),
            Product("Vans Old Skool", 60)
        ]
        all_sports_shoes = []
        all_everyday_shoes = []

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