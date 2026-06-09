from backend.src.menu import Menu
from backend.src.kitchen import Kitchen
from backend.src.restaurant_system import RestaurantSystem
from backend.src.order import Order
from backend.src.command.order_controller import OrderController
from backend.src.command.place_order_command import PlaceOrderCommand
from backend.src.command.submit_order_command import SubmitOrderCommand

def test_submit_order_command_changes_status():
    """I use this to confirm the submit command changes an order to Submitted."""
    order = Order(1, "Dine-In")
    controller = OrderController()

    controller.set_command(SubmitOrderCommand(order))
    controller.run_command()

    assert order.status == "Submitted"

def test_place_order_command_adds_order_to_system():
    """I use this to confirm the place-order command stores the order in the system."""
    menu = Menu()
    kitchen = Kitchen()
    system = RestaurantSystem(menu, kitchen)
    order = Order(1, "Dine-In")
    controller = OrderController()

    controller.set_command(PlaceOrderCommand(system, order))
    controller.run_command()

    assert system.track_order(1) == order