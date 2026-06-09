from backend.src.order_item import OrderItem
from backend.src.strategy.pricing_strategy import PricingStrategy
from backend.src.strategy.dine_in_strategy import DineInStrategy
from backend.src.strategy.take_out_strategy import TakeOutStrategy
from backend.src.strategy.delivery_strategy import DeliveryStrategy
from backend.src.state.new_order_state import NewOrderState
from backend.src.state.order_state import OrderState
from backend.src.observer.order_observer import OrderObserver
from datetime import datetime


def get_pricing_strategy_for_order_type(order_type: str) -> PricingStrategy:
    """I use this to pick the correct pricing strategy for a given order type."""
    normalized_order_type = order_type.strip().lower()

    if normalized_order_type in {"delivery"}:
        return DeliveryStrategy()

    if normalized_order_type in {"takeout", "take-out", "take out"}:
        return TakeOutStrategy()

    return DineInStrategy()

class Order:
    def __init__(self, order_id: int, order_type: str, status: str = "New"):
        """I use this to build a new order with default state, strategy, and observers."""
        self.__order_id = order_id
        self.__order_type = order_type
        self.__items: list[OrderItem] = []
        self.__status = status
        self.__pricing_strategy: PricingStrategy = get_pricing_strategy_for_order_type(order_type)
        self.__state: OrderState = NewOrderState()
        self.__observers: list[OrderObserver] = []
        self.__submitted_at = None

    @property
    def order_id(self) -> int:
        """I use this to expose the order's numeric id."""
        return self.__order_id

    @property
    def order_type(self) -> str:
        """I use this to expose whether the order is dine-in, take-out, or delivery."""
        return self.__order_type

    @order_type.setter
    def order_type(self, order_type: str) -> None:
        """I use this to update the order type when a builder changes it."""
        self.__order_type = order_type
        self.__pricing_strategy = get_pricing_strategy_for_order_type(order_type)

    @property
    def items(self) -> list[OrderItem]:
        """I use this to expose the current list of order items."""
        return self.__items

    @property
    def status(self) -> str:
        """I use this to expose the readable status label."""
        return self.__status

    @status.setter
    def status(self, status: str) -> None:
        """I use this to force the status text when needed."""
        self.__status = status

    @property
    def submitted_at(self):
        """I use this to expose when the order was submitted."""
        return self.__submitted_at
    
    def get_order_id(self) -> int:
        """I use this to return the order id in places that expect a method call."""
        return self.__order_id

    def add_item(self, item: OrderItem) -> None:
        """I use this to add one item to the order."""
        self.__items.append(item)

    def remove_item(self, item: OrderItem) -> None:
        """I use this to remove one item if it exists in the order."""
        if item in self.__items:
            self.__items.remove(item)

    def set_pricing_strategy(self, strategy: PricingStrategy) -> None:
        """I use this to swap in the pricing rules for this order type."""
        self.__pricing_strategy = strategy
    
    def attach(self, observer: OrderObserver) -> None:
        """I use this to register a display that should react to status changes."""
        if observer not in self.__observers:
            self.__observers.append(observer)

    def detach(self, observer: OrderObserver) -> None:
        """I use this to stop sending updates to one observer."""
        if observer in self.__observers:
            self.__observers.remove(observer)

    def notify_observers(self) -> None:
        """I use this to broadcast the latest order state to every observer."""
        for observer in self.__observers:
            observer.update(self)

    def calculate_total(self) -> float:
        """I use this to calculate the order total through the active pricing strategy."""
        return self.__pricing_strategy.calculate_total(self)
    
    def change_state(self, new_state: OrderState) -> None:
        """I use this to switch states, refresh the status text, and notify observers."""
        self.__state = new_state
        self.__status = new_state.get_status_name()
        self.notify_observers()

    def submit_order(self) -> None:
        """I use this to stamp the submission time and trigger the submit transition."""
        self.__submitted_at = datetime.now()
        self.__state.submit(self)
    
    def send_to_kitchen(self) -> None:
        """I use this to move the order into the kitchen workflow."""
        self.__state.send_to_kitchen(self)

    def prepare_order(self) -> None:
        """I use this to move the order into the preparing state."""
        self.__state.prepare(self)

    def mark_ready(self) -> None:
        """I use this to mark the order as finished and ready."""
        self.__state.mark_ready(self)

    def __str__(self) -> str:
        """I use this to format the full order for console output."""
        item_lines = "\n".join(str(item) for item in self.__items)
        return (
            f"Order ID: {self.__order_id}\n"
            f"Order Type: {self.__order_type}\n"
            f"Status: {self.__status}\n"
            f"Items:\n{item_lines}\n"
            f"Total: ${self.calculate_total():.2f}"
        )
