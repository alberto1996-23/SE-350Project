from typing import List
from backend.src.menu_item import MenuItem
from backend.src.factory.menu_factory import MenuCategoryFactory


class LunchFactory(MenuCategoryFactory):
    def create_items(self) -> List[MenuItem]:
        """I use this to build every lunch menu item."""
        return [
            MenuItem(
                "Pika Patty",
                "A Pikachu-themed burger with cheese, onions, lettuce, tomatoes, and condiments.",
                "Lunch",
                5.00
            ),
            MenuItem(
                "Farfetch’d Leek Salad",
                "A salad with cucumbers, chopped leek, and choice of fruits and veggies.",
                "Lunch",
                4.00
            ),
            MenuItem(
                "Fried Magikarp Strips",
                "Fish strips served with chips and a drink choice.",
                "Lunch",
                7.50
            ),
        ]
