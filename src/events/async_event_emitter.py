"""Asynchronous publish/subscribe event emitter."""
from typing import Callable, Dict, List, Any

class AsyncEventEmitter:
    def __init__(self):
        self._listeners: Dict[str, List[Callable[[Any], None]]] = {}

    def on(self, event: str, listener: Callable[[Any], None]):
        self._listeners.setdefault(event, []).append(listener)

    def emit(self, event: str, payload: Any = None):
        for listener in self._listeners.get(event, []):
            listener(payload)
