import LoadingMessage from '../components/LoadingMessage'
import ErrorMessage from '../components/ErrorMessage'
import useOrderStatus from '../hooks/useOrderStatus'

type OrderStatusPageProps = {
  orderId: number | null
}

function OrderStatusPage({ orderId }: OrderStatusPageProps) {
  // I use this page to show the current order number, items, and status text.
  const { status, loading, error } = useOrderStatus(orderId)

  if (orderId === null) {
    return <ErrorMessage message="No order has been submitted yet." />
  }

  if (loading) {
    return <LoadingMessage message="Checking order status..." />
  }

  if (error !== '') {
    return <ErrorMessage message={error} />
  }

  if (status === null) {
    return <ErrorMessage message="No status found." />
  }

  return (
    <section className="status-page">
      <div className="status-card">
        <h2 className="status-heading">Order Status</h2>
        <p>Order ID: {status.order_id}</p>
        <p>Order Type: {status.order_type ?? 'Unknown'}</p>
        <p>Status: {status.status ?? 'Unknown'}</p>
        <p>{getStatusMessage(status.status)}</p>

        <div className="status-items">
          <h3>Items in your order</h3>
          <ul>
            {status.items.map((item, index) => (
              <li key={`${item.name}-${index}`}>
                <span>{item.name} x{item.quantity}</span>
                <span>${item.subtotal.toFixed(2)}</span>
              </li>
            ))}
          </ul>
        </div>

        <p>Total: ${typeof status.total === 'number' ? status.total.toFixed(2) : '0.00'}</p>
      </div>
    </section>
  )
}

function getStatusMessage(status: string) {
  // I use this to translate raw backend statuses into friendlier messages.
  if (status === 'New') {
    return 'Your order was received.'
  }

  if (status === 'Submitted') {
    return 'Your order was submitted successfully.'
  }

  if (status === 'In Kitchen' || status === 'Preparing') {
    return 'Your food is being prepared right now.'
  }

  if (status === 'Ready') {
    return 'Your order is ready for pickup!'
  }

  return ''
}

export default OrderStatusPage