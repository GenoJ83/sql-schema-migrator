import heapq
from typing import Any, Tuple

class BoundedPriorityQueue:
    def __init__(self, maxsize: int = 100):
        self.maxsize = maxsize
        self._heap: list = []
        self._counter = 0

    def push(self, item: Any, priority: int = 10) -> bool:
        if len(self._heap) >= self.maxsize:
            return False
        # Lower priority number = processed first
        heapq.heappush(self._heap, (priority, self._counter, item))
        self._counter += 1
        return True

    def pop(self) -> Any:
        if not self._heap:
            raise IndexError("pop from an empty priority queue")
        return heapq.heappop(self._heap)[2]

    def size(self) -> int:
        return len(self._heap)
