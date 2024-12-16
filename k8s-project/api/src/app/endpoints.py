# app/endpoints.py
from fastapi import APIRouter, HTTPException
from app.cache import get_from_cache, cache_response
import time

router = APIRouter()

@router.get("/data/{item_id}")
async def get_data(item_id: str):
    cache_key = f"item_data_{item_id}"
    
    # First, check if data is available in the cache
    cached_data = get_from_cache(cache_key)
    
    if cached_data:
        # If cached, return it directly
        return {"data": cached_data, "source": "cache"}

    # Simulate a backend call (e.g., API or database query)
    time.sleep(2)  # Simulating delay (can be a slow API or DB query)
    
    # Simulated data
    data = {"item_id": item_id, "data": "Some data for the item"}

    # Store in cache for future requests
    cache_response(cache_key, data)
    
    return {"data": data, "source": "new"}

@router.get("/static-data")
async def get_static_data():
    """Simple endpoint to simulate a static resource"""
    return {"message": "This is static data and will not be cached."}
