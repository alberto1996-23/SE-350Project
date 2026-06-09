// This hook should:

// fetch one order’s status
// optionally poll every few seconds
// return { data, loading, error }

// That way the page stays simple.
import { useEffect, useState } from 'react'
import { fetchOrderStatus } from '../services/api'
import type { OrderStatusResponse } from '../types/api'

function useOrderStatus(orderId: number | null) {
  // I use this hook to poll the backend for the latest status of one order.
  const [status, setStatus] = useState<OrderStatusResponse | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  useEffect(() => {
    if (orderId === null) {
      return
    }

    const currentOrderId = orderId
    let cancelled = false

    async function loadStatus() {
      // I use this to fetch the latest status snapshot and update the hook state.
      try {
        setLoading(true)
        setError('')

        const data = await fetchOrderStatus(currentOrderId)
        console.log('order status response:', data)

        if (cancelled === false) {
          setStatus(data)
        }
      } catch {
        if (cancelled === false) {
          setError('Could not load order status.')
        }
      } finally {
        if (cancelled === false) {
          setLoading(false)
        }
      }
    }

    loadStatus()

    const intervalId = window.setInterval(loadStatus, 3000)

    return () => {
      cancelled = true
      window.clearInterval(intervalId)
    }
  }, [orderId])

  return { status, loading, error }
}

export default useOrderStatus