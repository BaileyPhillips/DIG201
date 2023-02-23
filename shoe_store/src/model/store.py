class Store:
    def __init__(self, name):
        self._name = name
        self._categories = []

    def get_name(self):
        return self._name

    def get_categories(self):
        return self._categories

    def get_category_by_index(self, index):
        return self._categories[index]

    def get_category_by_name(self, name):
        for cat in self._categories:
            if cat.get_name() == name:
                return cat
        return None

    def add_category(self, category_object):
        self._categories.append(category_object)

    def add_all_categories(self, category_list):
        for category in category_list:
            self.add_category(category)

    def __str__(self):
        return self._name

