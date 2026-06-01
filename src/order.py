from order_item import OrderItem
from strategy.pricing_strategy import PricingStrategy
from strategy.dine_in_strategy import DineInStrategy
from state.new_order_state import NewOrderState
from state.order_state import OrderState

class Order:
    def __init__(self, order_id: int, order_type: str, status: str = "New"):
        self.__order_id = order_id
        self.__order_type = order_type
        self.__items: list[OrderItem] = []
        self.__status = status
        self.__pricing_strategy: PricingStrategy = DineInStrategy()
        self.__state: OrderState = NewOrderState()

    @property
    def order_id(self) -> int:
        return self.__order_id

    @property
    def order_type(self) -> str:
        return self.__order_type

    @order_type.setter
    def order_type(self, order_type: str) -> None:
        self.__order_type = order_type

    @property
    def items(self) -> list[OrderItem]:
        return self.__items

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str) -> None:
        self.__status = status

    def add_item(self, item: OrderItem) -> None:
        self.__items.append(item)

    def remove_item(self, item: OrderItem) -> None:
        if item in self.__items:
            self.__items.remove(item)

    def set_pricing_strategy(self, strategy: PricingStrategy) -> None:
        self.__pricing_strategy = strategy

    def calculate_total(self) -> float:
        return self.__pricing_strategy.calculate_total(self)
    
    def change_state(self, new_state: OrderState) -> None:
        self.__state = new_state
        self.__status = new_state.get_status_name()

    def submit_order(self) -> None:
        self.__state.submit(self)
    
    def send_to_kitchen(self) -> None:
        self.__state.send_to_kitchen(self)

    def prepare_order(self) -> None:
        self.__state.prepare(self)

    def mark_ready(self) -> None:
        self.__state.mark_ready(self)

    def __str__(self) -> str:
        item_lines = "\n".join(str(item) for item in self.__items)
        return (
            f"Order ID: {self.__order_id}\n"
            f"Order Type: {self.__order_type}\n"
            f"Status: {self.__status}\n"
            f"Items:\n{item_lines}\n"
            f"Total: ${self.calculate_total():.2f}"
        )
