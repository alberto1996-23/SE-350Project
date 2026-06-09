from backend.src.command.command import Command
from backend.src.order import Order
from backend.src.restaurant_system import RestaurantSystem


class SendToKitchenCommand(Command):
    def __init__(self, restaurant_system: RestaurantSystem, order: Order):
        """I use this to remember which order should be sent into the kitchen."""
        self.__restaurant_system = restaurant_system
        self.__order = order

    def execute(self) -> None:
        """I use this to pass the stored order to the restaurant system's kitchen flow."""
        self.__restaurant_system.send_to_kitchen(self.__order)