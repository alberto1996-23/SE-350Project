from typing import List
from backend.src.menu_item import MenuItem
from backend.src.factory.menu_factory import MenuCategoryFactory


class DessertFactory(MenuCategoryFactory):
    def create_items(self) -> List[MenuItem]:
        """I use this to build every dessert menu item."""
        return [
            MenuItem(
                "Vanilluxe Ice Cream",
                "Vanilla ice cream served with sprinkles and whipped cream.",
                "Dessert",
                2.50
            ),
            MenuItem(
                "Appletun Turnover",
                "Apple turnover.",
                "Dessert",
                3.00
            ),
            MenuItem(
                "Alcremie Cake",
                "Vanilla or chocolate cake with whipped creme and a cherry on top.",
                "Dessert",
                6.00
            ),
        ]
