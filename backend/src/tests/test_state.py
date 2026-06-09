from backend.src.order import Order

def test_order_state_flow():
    """I use this to confirm the order moves through each expected state in order."""
    order = Order(1, "Dine-In")

    assert order.status == "New"

    order.submit_order()
    assert order.status == "Submitted"

    order.send_to_kitchen()
    assert order.status == "In Kitchen"

    order.prepare_order()
    assert order.status == "Preparing"

    order.mark_ready()
    assert order.status == "Ready"