from menu_item import MenuItem
from builder.dine_in_order_builder import DineInOrderBuilder


def main():
    burger = MenuItem("Pika Patty", "Burger with toppings", "Lunch", 5.00)
    fries = MenuItem("Fries", "Crispy fries", "Side", 2.00)

    builder = DineInOrderBuilder()
    builder.add_entree(burger, 2)
    builder.add_side(fries, 1)

    order = builder.build()
    print(order)


if __name__ == "__main__":
    main()
