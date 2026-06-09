from backend.src.menu_item import MenuItem

class Menu:
    def __init__(self):
        """I use this to start an empty menu with categories and items."""
        self.__categories: list[str] = []
        self.__items: list[MenuItem] = []

    def get_categories(self) -> list[str]:
        """I use this to return every category currently on the menu."""
        return self.__categories

    def get_items(self) -> list[MenuItem]:
        """I use this to return every menu item I have stored."""
        return self.__items

    def add_item(self, item: MenuItem) -> None:
        """I use this to add a new item and register its category if needed."""
        self.__items.append(item)

        category = item.category
        if category not in self.__categories:
            self.__categories.append(category)

    def remove_item(self, item: MenuItem) -> None:
        """I use this to remove an item if it already exists on the menu."""
        if item in self.__items:
            self.__items.remove(item)

    def get_items_by_category(self, category: str) -> list[MenuItem]:
        """I use this to pull just the items for one category."""
        return [item for item in self.__items if item.category == category]

    def find_item_by_name(self, name: str) -> MenuItem | None:
        """I use this to find one menu item by its name."""
        for item in self.__items:
            if item.name == name:
                return item
        return None

    def display_menu(self) -> None:
        """I use this to print the full menu to the console."""
        for item in self.__items:
            print(item)