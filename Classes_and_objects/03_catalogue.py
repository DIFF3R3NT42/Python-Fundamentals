from typing import List


class Catalogue:
    products = []

    def __init__(self, name: str):
        self.name = name


    @staticmethod
    def add_product(product_name: str) -> None:
        Catalogue.products.append(product_name)


    @staticmethod
    def get_by_letter(first_letter: str) -> List:
        by_letter_list = []
        for product in Catalogue.products:
            if product[0] == first_letter:
                by_letter_list.append(product)

        return by_letter_list


    def __repr__(self):
        sorted_items = sorted(Catalogue.products)
        items_str = "\n".join(sorted_items)
        return f"Items in the {self.name} catalogue:\n{items_str}"



catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)