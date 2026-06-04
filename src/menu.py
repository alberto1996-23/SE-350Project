from menu_item import MenuItem

class Menu:
    def __init__(self):
        self.__categories: list[str] = []
        self.__items: list[MenuItem] = []

    def get_categories(self) -> list[str]:
        return self.__categories

    def get_items(self) -> list[MenuItem]:
        return self.__items

    def add_item(self, item: MenuItem) -> None:
        self.__items.append(item)

        category = item.category
        if category not in self.__categories:
            self.__categories.append(category)

    def remove_item(self, item: MenuItem) -> None:
        if item in self.__items:
            self.__items.remove(item)

    def get_items_by_category(self, category: str) -> list[MenuItem]:
        return [item for item in self.__items if item.category == category]

    def find_item_by_name(self, name: str) -> MenuItem | None:
        for item in self.__items:
            if item.name == name:
                return item
        return None

    def display_menu(self) -> None:
        for item in self.__items:
            print(item)