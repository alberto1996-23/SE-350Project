# Use it for:

# data coming into the backend from React
# data going out of the backend back to React

# So this is not where your design-pattern classes go.
# This is where your API DTO-style shapes go.

# Examples of what should live there:

# MenuItemResponse
# OrderItemRequest
# CreateOrderRequest
# OrderResponse
# OrderStatusResponse

# Your backend routes should convert your real Python objects into these API-friendly shapes.
from typing import List

from pydantic import BaseModel


class MenuItemResponse(BaseModel):
    name: str
    description: str
    category: str
    price: float


class MenuCategoryResponse(BaseModel):
    category: str
    items: List[MenuItemResponse]


class OrderItemRequest(BaseModel):
    name: str
    quantity: int


class CreateOrderRequest(BaseModel):
    order_type: str
    items: List[OrderItemRequest]


class OrderItemResponse(BaseModel):
    name: str
    quantity: int
    subtotal: float


class OrderStatusItemSchema(BaseModel):
    name: str
    quantity: int
    subtotal: float


class OrderResponse(BaseModel):
    order_id: int
    order_type: str
    status: str
    items: List[OrderItemResponse]
    total: float


class OrderStatusResponse(BaseModel):
    order_id: int
    order_type: str
    status: str
    items: List[OrderStatusItemSchema]
    total: float