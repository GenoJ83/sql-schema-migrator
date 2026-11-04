"""Interactive shell prompt with command history."""
from typing import List, Optional

class InteractivePrompt:
    def __init__(self, commands: Optional[List[str]] = None):
        self.commands = commands or ["help", "status", "run", "exit"]
        self.history: List[str] = []

    def record_input(self, cmd_line: str):
        if cmd_line.strip():
            self.history.append(cmd_line.strip())

    def get_completions(self, prefix: str) -> List[str]:
        return [c for c in self.commands if c.startswith(prefix.lower())]
