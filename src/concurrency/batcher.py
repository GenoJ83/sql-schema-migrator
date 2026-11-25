from typing import List, Any

class EventBatcher:
    def __init__(self, batch_size: int = 10):
        self.batch_size = batch_size
        self._buffer: List[Any] = []

    def add(self, item: Any) -> List[Any]:
        self._buffer.append(item)
        if len(self._buffer) >= self.batch_size:
            flushed = list(self._buffer)
            self._buffer.clear()
            return flushed
        return []

    def flush(self) -> List[Any]:
        flushed = list(self._buffer)
        self._buffer.clear()
        return flushed
