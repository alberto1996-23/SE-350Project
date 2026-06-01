from command.command import Command
from order import Order


class PrepareOrderCommand(Command):
    def __init__(self, order: Order):
        self.__order = order

    def execute(self) -> None:
        self.__order.prepare_order()