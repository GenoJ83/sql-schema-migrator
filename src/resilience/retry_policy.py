"""Exponential backoff retry decorator with jitter."""
import time
import random
from typing import Callable, Any

def retry_call(fn: Callable[[], Any], max_attempts: int = 3, base_delay: float = 0.05) -> Any:
    attempt = 0
    while True:
        try:
            return fn()
        except Exception as e:
            attempt += 1
            if attempt >= max_attempts:
                raise e
            sleep_time = (base_delay * (2 ** (attempt - 1))) + random.uniform(0, 0.02)
            time.sleep(sleep_time)
