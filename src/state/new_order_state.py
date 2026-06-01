from state.order_state import OrderState
from state.submitted_order_state import SubmittedOrderState

class NewOrderState(OrderState):
    def submit(self, order: "Order") -> None:
        order.change_state(SubmittedOrderState())

    def send_to_kitchen(self, order: "Order") -> None:
        print("Cannot send a new order to the kitchen before it is submitted.")

    def prepare(self, order: "Order") -> None:
        print("Cannot prepare a new order.")

    def mark_ready(self, order: "Order") -> None:
        print("Cannot mark a new order as ready.")

    def get_status_name(self) -> str:
        return "New"