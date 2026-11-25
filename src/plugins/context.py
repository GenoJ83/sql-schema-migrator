from typing import Dict, Any

class PluginContext:
    def __init__(self, execution_id: str, config: Dict[str, Any] = None):
        self.execution_id = execution_id
        self.config = config or {}
        self.state: Dict[str, Any] = {}
        self.is_cancelled = False

    def set_value(self, key: str, value: Any) -> None:
        self.state[key] = value

    def get_value(self, key: str, default: Any = None) -> Any:
        return self.state.get(key, default)

    def cancel(self) -> None:
        self.is_cancelled = True
