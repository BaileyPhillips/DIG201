class Category:
    def __init__(self, name):
        self._name = name
        self._products = []

    def get_name(self):
        return self._name

    def get_products(self):
        return self._products

    def get_product_by_index(self, index):
        return self._products[index]

    def get_product_by_name(self, name):
        for product in self._products:
            if product.get_name() == name:
                return product
        return None

    def add_product(self, product_object):
        self._products.append(product_object)

    def add_all_products(self, list_of_products):
        for product in list_of_products:
            self.add_product(product)

    def __str__(self):
        return f"{self._name} with {len(self._products)} products"

    