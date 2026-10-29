"""Thread-safe LRU Cache with TTL (Time-To-Live) eviction."""
import time
from collections import OrderedDict
import threading
from typing import Any, Optional

class LRUTTLCache:
    def __init__(self, capacity: int = 100, default_ttl_sec: float = 300.0):
        self.capacity = capacity
        self.default_ttl = default_ttl_sec
        self.cache: OrderedDict[str, tuple[Any, float]] = OrderedDict()
        self.lock = threading.Lock()

    def get(self, key: str) -> Optional[Any]:
        with self.lock:
            if key not in self.cache:
                return None
            val, expiry = self.cache[key]
            if time.time() > expiry:
                del self.cache[key]
                return None
            self.cache.move_to_end(key)
            return val

    def set(self, key: str, value: Any, ttl_sec: Optional[float] = None):
        ttl = ttl_sec if ttl_sec is not None else self.default_ttl
        expiry = time.time() + ttl
        with self.lock:
            if key in self.cache:
                del self.cache[key]
            elif len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
            self.cache[key] = (value, expiry)
