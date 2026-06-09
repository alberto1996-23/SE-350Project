# This is the bigger one.

# It should handle:

# creating an order
# getting an order by id
# submitting an order
# sending an order to kitchen
# preparing an order
# marking an order ready

# This route should call your real Python classes:

# Order
# OrderItem
# RestaurantSystem
# your commands
# your state transitions

# So this is the bridge between React and your design-pattern code.
from fastapi import APIRouter, HTTPException

from backend.repository import (
    get_menu,
    get_order,
    save_order,
    generate_order_id,
    get_restaurant_system,
    get_dynamic_status,
)
from backend.schemas import (
    CreateOrderRequest,
    OrderResponse,
    OrderStatusResponse,
    OrderItemResponse,
    OrderStatusItemSchema,
)

from backend.src.order import Order
from backend.src.order_item import OrderItem

from backend.src.command.order_controller import OrderController
from backend.src.command.place_order_command import PlaceOrderCommand
from backend.src.command.submit_order_command import SubmitOrderCommand
from backend.src.command.send_to_kitchen_command import SendToKitchenCommand
from backend.src.command.prepare_order_command import PrepareOrderCommand
from backend.src.command.mark_order_ready_command import MarkOrderReadyCommand


router = APIRouter(prefix="/api/orders", tags=["orders"])


def build_order_response(order: Order) -> OrderResponse:
    """I use this to convert an order object into the full API response shape."""
    items_response = []

    for item in order.items:
        items_response.append(
            OrderItemResponse(
                name=item.get_menu_item().name,
                quantity=item.quantity,
                subtotal=item.get_subtotal(),
            )
        )

    return OrderResponse(
        order_id=order.get_order_id(),
        order_type=order.order_type,
        status=order.status,
        items=items_response,
        total=order.calculate_total(),
    )


def build_order_status_response(order: Order) -> OrderStatusResponse:
    """I use this to build the lighter status payload the status page polls."""
    current_status = get_dynamic_status(order)

    return OrderStatusResponse(
        order_id=order.get_order_id(),
        order_type=order.order_type,
        status=current_status,
        items=[
            OrderStatusItemSchema(
                name=item.get_menu_item().name,
                quantity=item.quantity,
                subtotal=item.get_subtotal(),
            )
            for item in order.items
        ],
        total=order.calculate_total(),
    )


@router.post("", response_model=OrderResponse)
def create_order(payload: CreateOrderRequest) -> OrderResponse:
    """I use this to create an order from the frontend payload and save it."""
    menu = get_menu()
    restaurant_system = get_restaurant_system()

    order_id = generate_order_id()
    order = Order(order_id, payload.order_type)

    for requested_item in payload.items:
        menu_item = menu.find_item_by_name(requested_item.name)

        if menu_item is None:
            raise HTTPException(
                status_code=404,
                detail=f"Menu item '{requested_item.name}' was not found."
            )

        order_item = OrderItem(menu_item, requested_item.quantity)
        order.add_item(order_item)

    controller = OrderController()
    controller.set_command(PlaceOrderCommand(restaurant_system, order))
    controller.run_command()

    save_order(order)
    return build_order_response(order)


@router.get("/{order_id}", response_model=OrderResponse)
def read_order(order_id: int) -> OrderResponse:
    """I use this to fetch one saved order by id."""
    order = get_order(order_id)

    if order is None:
        raise HTTPException(status_code=404, detail="Order not found.")

    return build_order_response(order)


@router.get("/{order_id}/status", response_model=OrderStatusResponse)
def read_order_status(order_id: int) -> OrderStatusResponse:
    """I use this to return the current status snapshot for one order."""
    order = get_order(order_id)

    if order is None:
        raise HTTPException(status_code=404, detail="Order not found.")

    return build_order_status_response(order)


@router.post("/{order_id}/submit", response_model=OrderStatusResponse)
def submit_order(order_id: int) -> OrderStatusResponse:
    """I use this to submit an order and immediately send it into the kitchen flow."""
    order = get_order(order_id)

    if order is None:
        raise HTTPException(status_code=404, detail="Order not found.")

    controller = OrderController()
    controller.set_command(SubmitOrderCommand(order))
    controller.run_command()

    restaurant_system = get_restaurant_system()
    controller.set_command(SendToKitchenCommand(restaurant_system, order))
    controller.run_command()

    return build_order_status_response(order)


@router.post("/{order_id}/send-to-kitchen", response_model=OrderStatusResponse)
def send_order_to_kitchen(order_id: int) -> OrderStatusResponse:
    """I use this to manually move an order into the kitchen."""
    order = get_order(order_id)

    if order is None:
        raise HTTPException(status_code=404, detail="Order not found.")

    restaurant_system = get_restaurant_system()

    controller = OrderController()
    controller.set_command(SendToKitchenCommand(restaurant_system, order))
    controller.run_command()

    return build_order_status_response(order)


@router.post("/{order_id}/prepare", response_model=OrderStatusResponse)
def prepare_order(order_id: int) -> OrderStatusResponse:
    """I use this to move an order into the preparing state."""
    order = get_order(order_id)

    if order is None:
        raise HTTPException(status_code=404, detail="Order not found.")

    controller = OrderController()
    controller.set_command(PrepareOrderCommand(order))
    controller.run_command()

    return build_order_status_response(order)


@router.post("/{order_id}/mark-ready", response_model=OrderStatusResponse)
def mark_order_ready(order_id: int) -> OrderStatusResponse:
    """I use this to mark an order as ready through the command layer."""
    order = get_order(order_id)

    if order is None:
        raise HTTPException(status_code=404, detail="Order not found.")

    controller = OrderController()
    controller.set_command(MarkOrderReadyCommand(order))
    controller.run_command()

    return build_order_status_response(order)