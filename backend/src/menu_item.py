class MenuItem:
    def __init__(self, name: str, description: str, category: str, base_price: float):
        """I use this to store the basic info for one menu item."""
        self.__name = name
        self.__description = description
        self.__category = category
        self.__base_price = base_price

    @property
    def name(self) -> str:
        """I use this to expose the item's display name."""
        return self.__name

    @property
    def description(self) -> str:
        """I use this to expose the item's description text."""
        return self.__description

    @property
    def category(self) -> str:
        """I use this to expose which menu category the item belongs to."""
        return self.__category

    @property
    def base_price(self) -> float:
        """I use this to expose the stored base price."""
        return self.__base_price

    def get_price(self) -> float:
        """I use this to return the price that should be charged for the item."""
        return self.__base_price

    def get_description(self) -> str:
        """I use this to return the item's description in plain text."""
        return self.__description

    def __str__(self) -> str:
        """I use this to format a menu item for quick printing."""
        return f"{self.__name} ({self.__category}) - ${self.__base_price:.2f}"