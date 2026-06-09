from backend.src.menu import Menu
from backend.src.kitchen import Kitchen
from backend.src.order import Order

class RestaurantSystem:
    def __init__(self, menu: Menu, kitchen: Kitchen):
        """I use this to tie the menu, kitchen, and placed orders together."""
        self.__menu = menu
        self.__kitchen = kitchen
        self.__orders: list[Order] = []

    def place_order(self, order: Order) -> None:
        """I use this to record a newly placed order in the system."""
        self.__orders.append(order)

    def send_to_kitchen(self, order: Order) -> None:
        """I use this to hand an order off to the kitchen."""
        self.__kitchen.receive_order(order)

    def track_order(self, order_id: int) -> Order | None:
        """I use this to find a placed order by id."""
        for order in self.__orders:
            if order.order_id == order_id:
                return order
        return None

    def display_menu(self) -> None:
        """I use this to print the menu through the shared menu object."""
        self.__menu.display_menu()