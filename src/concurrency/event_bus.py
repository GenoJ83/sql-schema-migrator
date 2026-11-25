import fnmatch
from typing import Callable, Dict, List, Any

class PriorityEventBus:
    def __init__(self):
        self._subscribers: Dict[str, List[Callable[[Any], Any]]] = {}

    def subscribe(self, topic_pattern: str, handler: Callable[[Any], Any]) -> None:
        self._subscribers.setdefault(topic_pattern, []).append(handler)

    def publish(self, topic: str, payload: Any) -> List[Any]:
        results = []
        for pattern, handlers in self._subscribers.items():
            if fnmatch.fnmatch(topic, pattern):
                for h in handlers:
                    results.append(h(payload))
        return results

    def clear(self) -> None:
        self._subscribers.clear()
