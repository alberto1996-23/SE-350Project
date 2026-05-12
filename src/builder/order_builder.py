from abc import ABC, abstractmethod
from menu_item import MenuItem
from order import Order


class OrderBuilder(ABC):
    @abstractmethod
    def reset(self) -> None:
        pass

    @abstractmethod
    def set_order_type(self, order_type: str) -> None:
        pass

    @abstractmethod
    def add_entree(self, item: MenuItem, quantity: int) -> None:
        pass

    @abstractmethod
    def add_side(self, item: MenuItem, quantity: int) -> None:
        pass

    @abstractmethod
    def add_drink(self, item: MenuItem, quantity: int) -> None:
        pass

    @abstractmethod
    def add_dessert(self, item: MenuItem, quantity: int) -> None:
        pass

    @abstractmethod
    def build(self) -> Order:
        pass
