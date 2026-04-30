from menu_item import MenuItem


class OrderItem:
    def __init__(
        self,
        menu_item: MenuItem,
        quantity: int,
        selected_size: str = "",
        special_instructions: str = ""
    ):
        self.menu_item = menu_item
        self.quantity = quantity
        self.selected_size = selected_size
        self.special_instructions = special_instructions

    def get_subtotal(self) -> float:
        return self.menu_item.get_price() * self.quantity

    def get_menu_item(self) -> MenuItem:
        return self.menu_item

    def __str__(self) -> str:
        details = f"{self.menu_item.name} x{self.quantity}"
        if self.selected_size:
            details += f" [{self.selected_size}]"
        if self.special_instructions:
            details += f" - Notes: {self.special_instructions}"
        details += f" -> ${self.get_subtotal():.2f}"
        return details