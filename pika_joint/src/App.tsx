import { useEffect, useState } from 'react'
import { Routes, Route, useNavigate, useParams } from 'react-router-dom'
import './App.css'

import Header from './components/Header'
import MenuCategory from './components/MenuCategory'
import OrderPanel from './components/OrderPanel'
import LoadingMessage from './components/LoadingMessage'
import ErrorMessage from './components/ErrorMessage'
import OrderStatusPage from './pages/OrderStatusPage'

import { fetchMenu, createOrder, submitOrder } from './services/api'
import type { MenuCategory as MenuCategoryType, MenuItem } from './types/api'

type LocalOrderItem = {
  name: string
  quantity: number
  price: number
}

const SALES_TAX_RATE = 0.07
const DELIVERY_FEE = 3.5

function HomePage() {
  // I use this page to load the menu, manage the cart, and submit the order.
  const navigate = useNavigate()

  const [menuCategories, setMenuCategories] = useState<MenuCategoryType[]>([])
  const [orderItems, setOrderItems] = useState<LocalOrderItem[]>([])
  const [orderType, setOrderType] = useState('Dine-In')
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')
  const [isSubmitting, setIsSubmitting] = useState(false)

  useEffect(() => {
    async function loadMenu() {
      // I use this to pull the menu from the backend when the page first loads.
      try {
        setLoading(true)
        setError('')
        const data = await fetchMenu()
        setMenuCategories(data)
      } catch {
        setError('Could not load menu from backend.')
      } finally {
        setLoading(false)
      }
    }

    loadMenu()
  }, [])

  function handleAddToOrder(item: MenuItem) {
    // I use this to add a menu item to the cart or bump its quantity if it is already there.
    setOrderItems((prevItems) => {
      const existingItem = prevItems.find((orderItem) => orderItem.name === item.name)

      if (existingItem !== undefined) {
        return prevItems.map((orderItem) => {
          if (orderItem.name === item.name) {
            return { ...orderItem, quantity: orderItem.quantity + 1 }
          }

          return orderItem
        })
      }

      return [...prevItems, { name: item.name, quantity: 1, price: item.price }]
    })
  }

  function handleIncrease(name: string) {
    // I use this to increase the quantity for one item in the cart.
    setOrderItems((prevItems) =>
      prevItems.map((item) => {
        if (item.name === name) {
          return { ...item, quantity: item.quantity + 1 }
        }

        return item
      }),
    )
  }

  function handleDecrease(name: string) {
    // I use this to decrease the quantity for one item and remove it if it hits zero.
    setOrderItems((prevItems) =>
      prevItems
        .map((item) => {
          if (item.name === name) {
            return { ...item, quantity: item.quantity - 1 }
          }

          return item
        })
        .filter((item) => item.quantity > 0),
    )
  }

  function handleOrderTypeChange(type: string) {
    // I use this to switch between dine-in, takeout, and delivery before checkout.
    setOrderType(type)
  }

  async function handleSubmitOrder() {
    // I use this to create the order, submit it, and move the user to the status page.
    if (orderItems.length === 0) {
      return
    }

    try {
      setIsSubmitting(true)
      setError('')

      const payload = {
        order_type: orderType,
        items: orderItems.map((item) => ({
          name: item.name,
          quantity: item.quantity,
        })),
      }

      const createdOrder = await createOrder(payload)
      await submitOrder(createdOrder.order_id)

      setOrderItems([])
      navigate(`/status/${createdOrder.order_id}`)
    } catch {
      setError('Could not submit order.')
    } finally {
      setIsSubmitting(false)
    }
  }

  const subtotal = orderItems.reduce((sum, item) => sum + item.price * item.quantity, 0)
  const salesTax = subtotal * SALES_TAX_RATE
  const deliveryFee = orderType === 'Delivery' ? DELIVERY_FEE : 0
  const total = subtotal + salesTax + deliveryFee

  if (loading) {
    return (
      <div className="app-container">
        <Header leftImage="/chef_pikachu.webp" rightImage="/chef_eevee.webp" />
        <LoadingMessage message="Loading menu..." />
      </div>
    )
  }

  return (
    <div className="app-container">
      <Header leftImage="/chef_pikachu.webp" rightImage="/chef_eevee.webp" />

      {error !== '' && <ErrorMessage message={error} />}

      <div className="content-layout">
        <main className="menu-column">
          <section className="menu-shell">
            <h2 className="menu-title">Menu</h2>

            {menuCategories.map((category) => (
              <MenuCategory
                key={category.category}
                title={category.category}
                items={category.items}
                onAddToOrder={handleAddToOrder}
              />
            ))}
          </section>
        </main>

        <div className="order-column">
          <OrderPanel
            orderItems={orderItems}
            orderType={orderType}
            subtotal={subtotal}
            salesTax={salesTax}
            deliveryFee={deliveryFee}
            total={total}
            isSubmitting={isSubmitting}
            onIncrease={handleIncrease}
            onDecrease={handleDecrease}
            onOrderTypeChange={handleOrderTypeChange}
            onSubmitOrder={handleSubmitOrder}
          />
        </div>
      </div>
    </div>
  )
}

function App() {
  // I use this to define the main app routes.
  return (
    <Routes>
      <Route path="/" element={<HomePage />} />
      <Route path="/status/:orderId" element={<StatusRouteWrapper />} />
    </Routes>
  )
}

function StatusRouteWrapper() {
  // I use this to turn the route param into a number before handing it to the status page.
  const params = useParams()
  const orderId = Number(params.orderId)

  if (Number.isNaN(orderId)) {
    return <OrderStatusPage orderId={null} />
  }

  return <OrderStatusPage orderId={orderId} />
}

export default App