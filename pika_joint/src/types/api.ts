// Put all frontend API types here.

// Things like:

// MenuItem
// MenuCategory
// OrderItem
// CreateOrderRequest
// OrderResponse
// OrderStatusResponse

// This file is just TypeScript types/interfaces.
export type MenuItem = {
  name: string
  description: string
  category: string
  price: number
}

export type OrderStatusItem = {
  name: string
  quantity: number
  subtotal: number
}

export type MenuCategory = {
  category: string
  items: MenuItem[]
}

export type CreateOrderItemRequest = {
  name: string
  quantity: number
}

export type CreateOrderRequest = {
  order_type: string
  items: CreateOrderItemRequest[]
}

export type OrderItemResponse = {
  name: string
  quantity: number
  subtotal: number
}

export type OrderResponse = {
  order_id: number
  order_type: string
  status: string
  items: OrderItemResponse[]
  total: number
}

export type OrderStatusResponse = {
  order_id: number
  order_type: string
  status: string
  items: OrderStatusItem[]
  total: number
}