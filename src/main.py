from menu_item import MenuItem
from order_item import OrderItem
from order import Order


def main():
    burger = MenuItem(
        "Pika Patty",
        "A Pikachu-themed burger with cheese, onions, lettuce, tomatoes, and condiments.",
        "Lunch",
        5.00
    )

    fries = MenuItem(
        "Fries",
        "Crispy fries served hot.",
        "Side",
        2.00
    )

    burger_order_item = OrderItem(burger, 2)
    fries_order_item = OrderItem(fries, 1, "Medium")

    order = Order(1, "Dine-In")
    order.add_item(burger_order_item)
    order.add_item(fries_order_item)
    order.submit_order()

    print(order)


if __name__ == "__main__":
    main()