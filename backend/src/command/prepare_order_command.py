from backend.src.command.command import Command
from backend.src.order import Order


class PrepareOrderCommand(Command):
    def __init__(self, order: Order):
        """I use this to remember which order should be prepared."""
        self.__order = order

    def execute(self) -> None:
        """I use this to trigger the order's preparing transition."""
        self.__order.prepare_order()