type MenuItemCardProps = {
  name: string
  description: string
  price: number
  onAddToOrder: () => void
}

function MenuItemCard({ name, description, price, onAddToOrder }: MenuItemCardProps) {
  // I use this to show one menu item with its add-to-order button.
  return (
    <article className="menu-item-card">
      <div className="menu-item-header">
        <h3 className="menu-item-name">{name}</h3>
        <span className="menu-item-price">${price.toFixed(2)}</span>
      </div>

      <p className="menu-item-description">{description}</p>

      <div className="menu-item-actions">
        <button className="add-button" onClick={onAddToOrder}>
          Add to Order
        </button>
      </div>
    </article>
  )
}

export default MenuItemCard