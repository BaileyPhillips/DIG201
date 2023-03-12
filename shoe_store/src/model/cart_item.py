class CartItem:
    def __init__(self, product, size):
        self._product = product
        self._size = size


    def get_product(self):
        return self._product

    def get_size(self):
        return self._size
