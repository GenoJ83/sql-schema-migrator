from typing import Callable, List, Any

class InterceptorChain:
    def __init__(self):
        self.interceptors: List[Callable[[Any], Any]] = []

    def add_interceptor(self, fn: Callable[[Any], Any]) -> None:
        self.interceptors.append(fn)

    def process(self, payload: Any) -> Any:
        data = payload
        for fn in self.interceptors:
            data = fn(data)
        return data
