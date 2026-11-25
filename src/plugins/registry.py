from typing import Callable, Dict, List, Any

class HookRegistry:
    def __init__(self):
        self._hooks: Dict[str, List[tuple]] = {}

    def register(self, hook_name: str, callback: Callable, priority: int = 100) -> None:
        self._hooks.setdefault(hook_name, []).append((priority, callback))
        self._hooks[hook_name].sort(key=lambda item: item[0])

    def emit(self, hook_name: str, *args, **kwargs) -> List[Any]:
        results = []
        for _, cb in self._hooks.get(hook_name, []):
            results.append(cb(*args, **kwargs))
        return results

    def registered_hooks(self) -> List[str]:
        return list(self._hooks.keys())
