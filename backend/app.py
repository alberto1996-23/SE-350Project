# This should be the main backend entry point.

# It should:

# create the app
# enable CORS
# register menu routes
# register order routes
# start the server

# So app.py should be small. It should mostly wire everything together.
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routes.orders import router as orders_router
from backend.routes.menu import router as menu_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(menu_router)
app.include_router(orders_router)