from typing import Generator

# In-memory mock databases
fake_db = {
    "products": [
        {"id": 1, "name": "Laptop", "price": 55000.0, "stock": 10, "category": "Electronics"},
        {"id": 2, "name": "Smartphone", "price": 25000.0, "stock": 15, "category": "Electronics"},
        {"id": 3, "name": "Headphones", "price": 1999.0, "stock": 50, "category": "Accessories"},
        {"id": 4, "name": "T-Shirt", "price": 499.0, "stock": 100, "category": "Clothing"},
        {"id": 5, "name": "Shoes", "price": 2999.0, "stock": 40, "category": "Clothing"}
    ],
    "users": [
        {"id": 1, "name": "Alice Smith", "email": "alice@example.com"},
        {"id": 2, "name": "Bob Jones", "email": "bob@example.com"}
    ],
    "cart": [],
    "orders": [],
    "payments": []
}

class MockSession:
    """Mock session class to simulate SQL operations temporarily."""
    def query(self, entity):
        return MockQuery(entity)
    
    def add(self, instance):
        pass

    def commit(self):
        pass

    def refresh(self, instance):
        pass

class MockQuery:
    def __init__(self, entity):
        self.entity = entity
        self.table_name = getattr(entity, "__name__", str(entity)).lower()
        if "product" in self.table_name:
            self.data = fake_db["products"]
        elif "user" in self.table_name:
            self.data = fake_db["users"]
        else:
            self.data = []

    def all(self):
        return self.data

    def filter(self, *args, **kwargs):
        return self

    def first(self):
        return self.data[0] if self.data else None

def get_db() -> Generator:
    """Dependency injection for database session."""
    db = MockSession()
    try:
        yield db
    finally:
        pass