from abc import ABC, abstractmethod
from backend.src.menu_item import MenuItem
from backend.src.order import Order


class OrderBuilder(ABC):
    @abstractmethod
    def reset(self) -> None:
        """I use this to clear the builder and start a fresh order."""
        pass

    @abstractmethod
    def set_order_type(self, order_type: str) -> None:
        """I use this to change the order type the builder is making."""
        pass

    @abstractmethod
    def add_entree(self, item: MenuItem, quantity: int) -> None:
        """I use this to add an entree to the order being built."""
        pass

    @abstractmethod
    def add_side(self, item: MenuItem, quantity: int) -> None:
        """I use this to add a side to the order being built."""
        pass

    @abstractmethod
    def add_drink(self, item: MenuItem, quantity: int) -> None:
        """I use this to add a drink to the order being built."""
        pass

    @abstractmethod
    def add_dessert(self, item: MenuItem, quantity: int) -> None:
        """I use this to add a dessert to the order being built."""
        pass

    @abstractmethod
    def build(self) -> Order:
        """I use this to return the completed order and reset the builder."""
        pass
