from backend.src.order import Order
from backend.src.observer.customer_display import CustomerDisplay
from backend.src.observer.kitchen_display import KitchenDisplay
from backend.src.observer.cashier_display import CashierDisplay

def test_observers_are_notified_on_state_change(capsys):
    """I use this to confirm every observer prints when the order state changes."""
    order = Order(1, "Dine-In")

    order.attach(CustomerDisplay(order))
    order.attach(KitchenDisplay(order))
    order.attach(CashierDisplay(order))

    order.submit_order()

    captured = capsys.readouterr()
    output = captured.out

    assert "[Customer Display]" in output
    assert "[Kitchen Display]" in output
    assert "[Cashier Display]" in output
    assert "Submitted" in output