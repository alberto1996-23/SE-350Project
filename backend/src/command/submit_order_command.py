from backend.src.command.command import Command
from backend.src.order import Order

class SubmitOrderCommand(Command):
    def __init__(self, order: Order):
        """I use this to remember which order should be submitted."""
        self.__order = order

    def execute(self) -> None:
        """I use this to trigger the order's submit transition."""
        self.__order.submit_order()