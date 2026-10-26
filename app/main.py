from fastapi import FastAPI
from app.routers import products, users, orders, cart, payments

app = FastAPI(title="E-commerce Backend API")

# Include Routers
app.include_router(products.router)
app.include_router(users.router)
app.include_router(orders.router)
app.include_router(cart.router)
app.include_router(payments.router)

@app.get("/")
def root():
    return {"message": "Welcome to the E-commerce Backend System! Go to /docs for Swagger UI."}