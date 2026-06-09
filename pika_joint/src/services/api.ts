// This should be your frontend fetch layer.

// It should contain functions like:

// fetchMenu()
// createOrder()
// getOrderStatus(orderId)
// submitOrder(orderId)
// sendOrderToKitchen(orderId)
// prepareOrder(orderId)
// markOrderReady(orderId)

// This keeps App.tsx and your components clean.
import type {
  MenuCategory,
  CreateOrderRequest,
  OrderResponse,
  OrderStatusResponse,
} from '../types/api'

const API_BASE_URL = 'http://127.0.0.1:8000'

async function handleResponse<T>(response: Response): Promise<T> {
  // I use this to turn failed fetches into real errors and parse successful JSON.
  if (!response.ok) {
    const errorText = await response.text()
    throw new Error(errorText || 'Request failed')
  }

  return response.json() as Promise<T>
}

export async function fetchMenu(): Promise<MenuCategory[]> {
  // I use this to fetch the grouped menu from the backend.
  const response = await fetch(`${API_BASE_URL}/api/menu`)
  return handleResponse<MenuCategory[]>(response)
}

export async function createOrder(payload: CreateOrderRequest): Promise<OrderResponse> {
  // I use this to send a brand-new order to the backend.
  const response = await fetch(`${API_BASE_URL}/api/orders`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(payload),
  })

  return handleResponse<OrderResponse>(response)
}

export async function submitOrder(orderId: number): Promise<OrderStatusResponse> {
  // I use this to submit one order and start its kitchen flow.
  const response = await fetch(`${API_BASE_URL}/api/orders/${orderId}/submit`, {
    method: 'POST',
  })

  return handleResponse<OrderStatusResponse>(response)
}

export async function sendOrderToKitchen(orderId: number): Promise<OrderStatusResponse> {
  // I use this to manually push an order into the kitchen endpoint if I need to.
  const response = await fetch(`${API_BASE_URL}/api/orders/${orderId}/send-to-kitchen`, {
    method: 'POST',
  })

  return handleResponse<OrderStatusResponse>(response)
}

export async function fetchOrderStatus(orderId: number): Promise<OrderStatusResponse> {
  // I use this to fetch the current status payload for one order.
  const response = await fetch(`${API_BASE_URL}/api/orders/${orderId}/status`)
  return handleResponse<OrderStatusResponse>(response)
}