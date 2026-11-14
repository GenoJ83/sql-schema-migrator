"""Unit tests for LRU Cache with TTL expiration."""
from src.cache.lru_ttl_cache import LRUTTLCache

def test_lru_cache_capacity():
    cache = LRUTTLCache(capacity=2)
    cache.set("a", 1)
    cache.set("b", 2)
    cache.set("c", 3) # Should evict "a"
    assert cache.get("a") is None
    assert cache.get("b") == 2
    assert cache.get("c") == 3

def test_lru_cache_update():
    cache = LRUTTLCache(capacity=2)
    cache.set("x", 10)
    assert cache.get("x") == 10
    cache.set("x", 20)
    assert cache.get("x") == 20
