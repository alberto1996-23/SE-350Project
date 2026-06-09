import MenuItemCard from './MenuItemCard'
import type { MenuItem } from '../types/api'

type MenuCategoryProps = {
  title: string
  items: MenuItem[]
  onAddToOrder: (item: MenuItem) => void
}

function MenuCategory({ title, items, onAddToOrder }: MenuCategoryProps) {
  // I use this to render one menu section and all of its item cards.
  return (
    <section className="menu-category">
      <h2 className="menu-category-title">{title}</h2>

      <div className="menu-items-grid">
        {items.map((item) => (
          <MenuItemCard
            key={item.name}
            name={item.name}
            description={item.description}
            price={item.price}
            onAddToOrder={() => onAddToOrder(item)}
          />
        ))}
      </div>
    </section>
  )
}

export default MenuCategory