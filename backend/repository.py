# create and store one Menu
# create and store one Kitchen
# create and store one RestaurantSystem
# store orders in a dictionary by id
# generate the next order id
from backend.src.menu import Menu
from backend.src.kitchen import Kitchen
from backend.src.restaurant_system import RestaurantSystem
from backend.src.order import Order

from backend.src.factory.breakfast_factory import BreakfastFactory
from backend.src.factory.lunch_factory import LunchFactory
from backend.src.factory.dinner_factory import DinnerFactory
from backend.src.factory.dessert_factory import DessertFactory
from datetime import datetime


# Shared backend objects
menu = Menu()
kitchen = Kitchen()
restaurant_system = RestaurantSystem(menu, kitchen)

# In-memory order storage
orders_by_id: dict[int, Order] = {}
next_order_id = 1


def seed_menu() -> None:
    """I use this to load the shared menu with all factory-created items once."""
    factories = [
        BreakfastFactory(),
        LunchFactory(),
        DinnerFactory(),
        DessertFactory()
    ]

    for factory in factories:
        items = factory.create_items()
        for item in items:
            menu.add_item(item)


def get_menu() -> Menu:
    """I use this to return the shared menu instance."""
    return menu


def get_kitchen() -> Kitchen:
    """I use this to return the shared kitchen instance."""
    return kitchen


def get_restaurant_system() -> RestaurantSystem:
    """I use this to return the shared restaurant system instance."""
    return restaurant_system


def generate_order_id() -> int:
    """I use this to hand out the next available in-memory order id."""
    global next_order_id
    current_id = next_order_id
    next_order_id += 1
    return current_id


def save_order(order: Order) -> None:
    """I use this to save an order in the in-memory dictionary."""
    orders_by_id[order.get_order_id()] = order


def get_order(order_id: int) -> Order | None:
    """I use this to look up one order by id."""
    return orders_by_id.get(order_id)


def get_all_orders() -> list[Order]:
    """I use this to return every saved order."""
    return list(orders_by_id.values())


def get_dynamic_status(order):
    """I use this to advance time-based statuses for the order status page."""
    if order.submitted_at is None:
        return order.status

    now = datetime.now()
    seconds_passed = (now - order.submitted_at).total_seconds()
    item_count = len(order.items)
    ready_time = max(5, item_count * 3)

    if seconds_passed >= ready_time and order.status != "Ready":
        if order.status == "In Kitchen":
            order.prepare_order()
        if order.status == "Preparing":
            order.mark_ready()

    return order.status

seed_menu()