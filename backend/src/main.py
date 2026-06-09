from backend.src.menu import Menu
from backend.src.kitchen import Kitchen
from backend.src.restaurant_system import RestaurantSystem
from backend.src.menu_item import MenuItem
from backend.src.order_item import OrderItem
from backend.src.order import Order

from backend.src.command.order_controller import OrderController
from backend.src.command.place_order_command import PlaceOrderCommand
from backend.src.command.submit_order_command import SubmitOrderCommand
from backend.src.command.send_to_kitchen_command import SendToKitchenCommand
from backend.src.command.prepare_order_command import PrepareOrderCommand
from backend.src.command.mark_order_ready_command import MarkOrderReadyCommand
from backend.src.observer.customer_display import CustomerDisplay
from backend.src.observer.kitchen_display import KitchenDisplay
from backend.src.observer.cashier_display import CashierDisplay

def main():
    """I use this to run a full console demo of the restaurant workflow."""
    menu = Menu()
    kitchen = Kitchen()
    restaurant_system = RestaurantSystem(menu, kitchen)
    controller = OrderController()

    burger = MenuItem("Pika Patty", "Burger with toppings", "Lunch", 5.00)
    fries = MenuItem("Fries", "Crispy fries", "Side", 2.00)

    menu.add_item(burger)
    menu.add_item(fries)

    order = Order(1, "Dine-In")
    order.add_item(OrderItem(burger, 2))
    order.add_item(OrderItem(fries, 1))

    customer_display = CustomerDisplay(order)
    kitchen_display = KitchenDisplay(order)
    cashier_display = CashierDisplay(order)

    order.attach(customer_display)
    order.attach(kitchen_display)
    order.attach(cashier_display)

    controller.set_command(PlaceOrderCommand(restaurant_system, order))
    controller.run_command()
    print("\nAfter place:")
    print(order)

    controller.set_command(SubmitOrderCommand(order))
    controller.run_command()
    print("\nAfter submit:")
    print(order)

    controller.set_command(SendToKitchenCommand(restaurant_system, order))
    controller.run_command()
    print("\nAfter send to kitchen:")
    print(order)

    controller.set_command(PrepareOrderCommand(order))
    controller.run_command()
    print("\nAfter prepare:")
    print(order)

    controller.set_command(MarkOrderReadyCommand(order))
    controller.run_command()
    print("\nAfter mark ready:")
    print(order)


if __name__ == "__main__":
    main()