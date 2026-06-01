from state.order_state import OrderState
from state.ready_state import ReadyState

class PreparingState(OrderState):
    def submit(self, order: "Order") -> None:
        print("Order is already being worked on.")

    def send_to_kitchen(self, order: "Order") -> None:
        print("Order is already in progress in the kitchen.")

    def prepare(self, order: "Order") -> None:
        print("Order is already being prepared.")

    def mark_ready(self, order: "Order") -> None:
        order.change_state(ReadyState())

    def get_status_name(self) -> str:
        return "Preparing"