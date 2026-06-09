# The Pika Joint - Startup Instructions and Project Details

## Overview

This project is my Pokémon-themed restaurant application. I built it with a Python backend and a React frontend. The idea is that a user can open the menu, add items to an order, choose an order type, submit the order, and then watch the order status move through the restaurant flow.

The main parts of the project are:

- `backend/` - my FastAPI backend and all of my design-pattern-based Python logic
- `pika_joint/` - my React + TypeScript frontend built with Vite

---

## How I Start the Program

I run the backend and frontend in separate terminals.

### 1. Start the backend

From the project root, I activate my virtual environment and run Uvicorn:

```bash
source .venv/bin/activate
uvicorn backend.app:app --reload
```

What this does:

- activates my Python virtual environment
- starts the FastAPI app from `backend/app.py`
- runs the backend in reload mode so changes are picked up automatically

The backend runs at:

- `http://127.0.0.1:8000`

### 2. Start the frontend

In another terminal, I go into the frontend folder and start the Vite dev server:

```bash
cd pika_joint
npm install
npm run dev
```

What this does:

- installs frontend dependencies if needed
- starts the React app in development mode

The frontend normally runs at:

- `http://localhost:5173`

### 3. Use the app

Once both servers are running, I open the frontend URL in the browser. From there I can:

- browse menu categories
- add items to the order panel
- choose dine-in or takeout
- submit the order
- move to the order status page automatically

---

## Backend Details

## What backend framework I used

I used **FastAPI** for the backend API.

My backend entry point is in `backend/app.py`. That file:

- creates the FastAPI app
- enables CORS
- registers the menu routes
- registers the order routes

I allowed the frontend dev server origin so the React app can call the backend while both are running locally.

## How my backend is organized

I split the backend into two main layers:

### 1. API layer

This is the part that the frontend talks to directly.

- `backend/routes/menu.py`
- `backend/routes/orders.py`
- `backend/schemas.py`
- `backend/repository.py`

What these files do:

- `menu.py` returns grouped menu data
- `orders.py` handles order creation, submission, and status reads
- `schemas.py` defines the request/response shapes used by the API
- `repository.py` stores shared in-memory objects like the menu, restaurant system, and saved orders

### 2. Core restaurant logic

This is the part where I implemented the actual restaurant behavior and design patterns.

That logic lives under `backend/src/`.

Important files include:

- `order.py`
- `order_item.py`
- `menu.py`
- `menu_item.py`
- `restaurant_system.py`
- `kitchen.py`

## Design patterns I used in the backend

I organized the backend around several design patterns for the restaurant flow.

### Command pattern

I used command classes to trigger restaurant actions in a structured way.

Examples:

- `PlaceOrderCommand`
- `SubmitOrderCommand`
- `SendToKitchenCommand`
- `PrepareOrderCommand`
- `MarkOrderReadyCommand`

These commands are coordinated through `OrderController`.

### State pattern

I used the state pattern so an order can move through a real workflow.

My states are:

- `New`
- `Submitted`
- `In Kitchen`
- `Preparing`
- `Ready`

This logic is handled in:

- `backend/src/state/new_order_state.py`
- `backend/src/state/submitted_order_state.py`
- `backend/src/state/in_kitchen_state.py`
- `backend/src/state/preparing_state.py`
- `backend/src/state/ready_state.py`

### Observer pattern

I used observers to simulate different parts of the restaurant reacting to order status changes.

Examples:

- customer display
- kitchen display
- cashier display

### Strategy pattern

I used pricing strategies so the total can be calculated differently depending on order type.

Examples:

- dine-in strategy
- take-out strategy
- delivery strategy

### Factory pattern

I used factories to seed the menu with category-based items like breakfast, lunch, dinner, and dessert.

### Builder pattern

I also included builders for creating different order types in a more structured way.

---

## How the backend works during an order

When I submit an order from the frontend, this is the general flow:

1. the frontend sends the order payload to `POST /api/orders`
2. the backend creates the order and saves it in memory
3. the frontend calls the submit endpoint
4. the backend moves the order into the kitchen workflow
5. the status page polls the backend for updates
6. the backend returns status, item list, and total
7. after a short delay, the order transitions to `Ready`

Important API endpoints include:

- `GET /api/menu`
- `POST /api/orders`
- `GET /api/orders/{order_id}`
- `GET /api/orders/{order_id}/status`
- `POST /api/orders/{order_id}/submit`

## Backend data behavior

Right now, my orders are stored **in memory**. That means:

- orders are not saved to a database
- restarting the backend clears the current saved orders
- this is fine for my project demo and local testing

---

## Frontend Details

## What frontend stack I used

I built the frontend with:

- **React**
- **TypeScript**
- **Vite**
- **React Router**

The frontend code is inside `pika_joint/src/`.

## How my frontend is organized

Important frontend files include:

- `App.tsx`
- `services/api.ts`
- `pages/OrderStatusPage.tsx`
- `hooks/useOrderStatus.ts`
- `components/OrderPanel.tsx`
- `components/MenuCategory.tsx`
- `components/MenuItemCard.tsx`
- `components/Header.tsx`

## How the frontend works

### Home page flow

On the home page, my frontend does the following:

1. loads menu data from the backend
2. displays menu categories and items
3. lets the user add items to the order
4. tracks quantities in the order panel
5. calculates the live total on the client side
6. submits the order to the backend
7. redirects to the order status page

`App.tsx` handles most of that top-level flow.

### API communication

I kept my frontend fetch logic in `pika_joint/src/services/api.ts`.

That file is responsible for:

- fetching the menu
- creating the order
- submitting the order
- fetching the order status

I did that so my components stay cleaner and do not all contain raw fetch calls.

### Order status page

After the user submits an order, the app navigates to the status route.

That page:

- shows the order number
- shows the order type
- shows the current status
- shows every item in the order
- shows the total cost

The polling logic is handled by `useOrderStatus.ts`.

That hook asks the backend for updates every few seconds so the UI can refresh automatically.

## Frontend styling

The visual styling is mainly handled by:

- `App.css`
- `index.css`

I styled the app to match the Pokémon restaurant theme with a cleaner menu layout and a separate order panel.

---

## Notes for Running the Project Smoothly

- I make sure the backend is running before I try to use the frontend.
- I make sure the frontend is running on the Vite dev server.
- If the status page fails, I check that the backend is still running.
- If I restart the backend, I know my in-memory orders will be reset.

---

## Quick Start Summary

If I want the shortest version possible, I do this:

### Backend terminal

```bash
source .venv/bin/activate
uvicorn backend.app:app --reload
```

### Frontend terminal

```bash
cd pika_joint
npm install
npm run dev
```

Then I open:

- `http://localhost:5173`

---

## Final Summary

This project is my full-stack restaurant system demo. The backend handles the actual order workflow using design patterns, and the frontend gives the user a simple interface for browsing the menu, building an order, submitting it, and tracking status updates.

The main idea is that the frontend is the interactive restaurant UI, while the backend is the part that actually manages the order lifecycle.
