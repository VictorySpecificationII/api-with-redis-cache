# app/db_endpoints.py
from fastapi import APIRouter, HTTPException
from app.cache import get_from_memcache, cache_to_memcache
import psycopg2
from psycopg2 import sql
from typing import Optional
import os

# Initialize Router
router = APIRouter()

# Database connection parameters
DB_CONFIG = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "postgres",
    "host": "postgresql.default.svc.cluster.local",
    "port": 5432,
}

# Initialize or verify table exists
def create_products_table():
    connection = psycopg2.connect(**DB_CONFIG)
    cursor = connection.cursor()
    create_table_query = """
    CREATE TABLE IF NOT EXISTS products (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        price REAL NOT NULL
    );
    """
    cursor.execute(create_table_query)
    connection.commit()
    cursor.close()
    connection.close()

@router.on_event("startup")
async def startup_event():
    """Ensure table exists when API starts."""
    create_products_table()

@router.post("/create-product/")
async def add_product(name: str, price: float):
    """Insert a new product into the database."""
    try:
        # Insert data
        connection = psycopg2.connect(**DB_CONFIG)
        cursor = connection.cursor()
        insert_query = "INSERT INTO products (name, price) VALUES (%s, %s) RETURNING id;"
        cursor.execute(insert_query, (name, price))
        product_id = cursor.fetchone()[0]
        connection.commit()
        cursor.close()
        connection.close()

        return {"message": "Product added successfully", "product_id": product_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get-product/{product_id}")
async def get_product(product_id: int):
    """Retrieve a product with optional caching."""
    cache_key = f"product_{product_id}"

    # First, check in Memcached
    cached_product = get_from_memcache(cache_key)
    if cached_product:
        return {"data": cached_product, "source": "cache"}

    try:
        # Fetch from DB
        connection = psycopg2.connect(**DB_CONFIG)
        cursor = connection.cursor()
        query = "SELECT id, name, price FROM products WHERE id = %s;"
        cursor.execute(query, (product_id,))
        product = cursor.fetchone()
        cursor.close()
        connection.close()

        if not product:
            raise HTTPException(status_code=404, detail="Product not found.")

        product_data = {"id": product[0], "name": product[1], "price": product[2]}

        # Add to Memcached
        cache_to_memcache(cache_key, product_data)
        return {"data": product_data, "source": "db"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
