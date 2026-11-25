import time
from typing import Dict, Any, List

class DeadLetterQueue:
    def __init__(self, max_retries: int = 3, base_delay: float = 1.0):
        self.max_retries = max_retries
        self.base_delay = base_delay
        self.failures: List[Dict[str, Any]] = []

    def record_failure(self, task_id: str, payload: Any, error: str, attempt: int) -> bool:
        can_retry = attempt < self.max_retries
        backoff = round(self.base_delay * (2 ** (attempt - 1)), 2) if can_retry else 0.0
        self.failures.append({
            "task_id": task_id,
            "error": error,
            "attempt": attempt,
            "can_retry": can_retry,
            "backoff_seconds": backoff,
            "timestamp": time.time()
        })
        return can_retry
