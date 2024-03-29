class Product:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def get_price_string(self):
        return "${:0.2f}".format(self._price)

    def __str__(self):
        return f"{self._name} {self.get_price_string()}"

