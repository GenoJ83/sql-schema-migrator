from typing import Dict

class PrometheusExporter:
    @staticmethod
    def format_counter(name: str, value: int, help_text: str = "") -> str:
        lines = []
        if help_text:
            lines.append(f"# HELP {name} {help_text}")
        lines.append(f"# TYPE {name} counter")
        lines.append(f"{name} {value}")
        return "\n".join(lines)

    @staticmethod
    def format_gauge(name: str, value: float, help_text: str = "") -> str:
        lines = []
        if help_text:
            lines.append(f"# HELP {name} {help_text}")
        lines.append(f"# TYPE {name} gauge")
        lines.append(f"{name} {value}")
        return "\n".join(lines)
