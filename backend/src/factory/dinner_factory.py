from typing import List
from backend.src.menu_item import MenuItem
from backend.src.factory.menu_factory import MenuCategoryFactory


class DinnerFactory(MenuCategoryFactory):
    def create_items(self) -> List[MenuItem]:
        """I use this to build every dinner menu item."""
        return [
            MenuItem(
                "Krabby Legs",
                "Crab legs served with butter and lemon.",
                "Dinner",
                6.00
            ),
            MenuItem(
                "Combusken Pesto Pasta",
                "Penne with pesto and chicken breast.",
                "Dinner",
                8.00
            ),
            MenuItem(
                "Peking Psyduck",
                "Chopped Psyduck with soy sauce and honey, served with ranch.",
                "Dinner",
                9.00
            ),
        ]
