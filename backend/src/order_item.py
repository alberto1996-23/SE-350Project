from backend.src.menu_item import MenuItem


class OrderItem:
    def __init__(
        self,
        menu_item: MenuItem,
        quantity: int,
        selected_size: str = "",
        special_instructions: str = ""
    ):
        """I use this to store one line item inside an order."""
        self.__menu_item = menu_item
        self.__quantity = quantity
        self.__selected_size = selected_size
        self.__special_instructions = special_instructions

    @property
    def menu_item(self) -> MenuItem:
        """I use this to expose the linked menu item."""
        return self.__menu_item

    @property
    def quantity(self) -> int:
        """I use this to expose how many of the item were ordered."""
        return self.__quantity

    @property
    def selected_size(self) -> str:
        """I use this to expose any chosen size option."""
        return self.__selected_size

    @property
    def special_instructions(self) -> str:
        """I use this to expose any custom notes for the item."""
        return self.__special_instructions

    def get_subtotal(self) -> float:
        """I use this to calculate this line item's subtotal."""
        return self.__menu_item.get_price() * self.__quantity

    def get_menu_item(self) -> MenuItem:
        """I use this to return the stored menu item object."""
        return self.__menu_item

    def __str__(self) -> str:
        """I use this to format the order item for quick debugging output."""
        details = f"{self.__menu_item.name} x{self.__quantity}"
        if self.__selected_size:
            details += f" [{self.__selected_size}]"
        if self.__special_instructions:
            details += f" - Notes: {self.__special_instructions}"
        details += f" -> ${self.get_subtotal():.2f}"
        return details
