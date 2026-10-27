"""Pluggable extension hook manager."""
from typing import Callable, Dict, List

class PluginManager:
    def __init__(self):
        self._hooks: Dict[str, List[Callable]] = {}

    def register_hook(self, hook_name: str, handler: Callable):
        self._hooks.setdefault(hook_name, []).append(handler)

    def trigger_hook(self, hook_name: str, *args, **kwargs) -> List[Any]:
        results = []
        for handler in self._hooks.get(hook_name, []):
            results.append(handler(*args, **kwargs))
        return results
