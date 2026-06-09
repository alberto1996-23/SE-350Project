type LocalOrderItem = {
  name: string
  quantity: number
  price: number
}

type OrderPanelProps = {
  orderItems: LocalOrderItem[]
  orderType: string
  total: number
  isSubmitting: boolean
  onIncrease: (name: string) => void
  onDecrease: (name: string) => void
  onOrderTypeChange: (type: string) => void
  onSubmitOrder: () => void
}

function OrderPanel({
  orderItems,
  orderType,
  total,
  isSubmitting,
  onIncrease,
  onDecrease,
  onOrderTypeChange,
  onSubmitOrder,
}: OrderPanelProps) {
  // I use this to show the live cart, order type picker, and submit button.
  return (
    <aside className="order-panel">
      <h2 className="order-panel-title">Your Order</h2>

      <div className="order-type-section">
        <select
          className="order-type-select"
          value={orderType}
          onChange={(e) => onOrderTypeChange(e.target.value)}
        >
          <option value="Dine-In">Dine-In</option>
          <option value="Takeout">Takeout</option>
        </select>
      </div>

      {orderItems.length === 0 && <p>No items added yet.</p>}

      {orderItems.length > 0 && (
        <>
          <div className="order-items-list">
            {orderItems.map((item) => (
              <div key={item.name} className="order-item">
                <div className="order-item-top">
                  <span className="order-item-name">{item.name}</span>
                  <span className="order-item-price">${item.price.toFixed(2)}</span>
                </div>

                <div className="order-item-controls">
                  <button className="qty-button" onClick={() => onDecrease(item.name)}>
                    -
                  </button>
                  <span className="qty-value">{item.quantity}</span>
                  <button className="qty-button" onClick={() => onIncrease(item.name)}>
                    +
                  </button>
                </div>
              </div>
            ))}
          </div>

          <div className="order-total">
            <span>Total</span>
            <span>${total.toFixed(2)}</span>
          </div>

          <button className="submit-button" onClick={onSubmitOrder} disabled={isSubmitting}>
            {isSubmitting ? 'Submitting...' : 'Submit'}
          </button>
        </>
      )}
    </aside>
  )
}

export default OrderPanel