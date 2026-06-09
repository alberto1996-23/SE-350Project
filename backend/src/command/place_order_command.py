from backend.src.command.command import Command
from backend.src.order import Order
from backend.src.restaurant_system import RestaurantSystem


class PlaceOrderCommand(Command):
    def __init__(self, restaurant_system: RestaurantSystem, order: Order):
        """I use this to remember which system and order the command should act on."""
        self.__restaurant_system = restaurant_system
        self.__order = order

    def execute(self) -> None:
        """I use this to place the stored order into the restaurant system."""
        self.__restaurant_system.place_order(self.__order)