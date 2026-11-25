"""ASCII formatted terminal grid table printer."""
from typing import List

class TerminalTablePrinter:
    @staticmethod
    def render_table(headers: List[str], rows: List[List[str]]) -> str:
        col_widths = [len(h) for h in headers]
        for row in rows:
            for idx, cell in enumerate(row):
                if idx < len(col_widths):
                    col_widths[idx] = max(col_widths[idx], len(str(cell)))

        sep = "+-" + "-+-".join("-" * w for w in col_widths) + "-+"
        head_line = "| " + " | ".join(h.ljust(col_widths[i]) for i, h in enumerate(headers)) + " |"
        body_lines = [
            "| " + " | ".join(str(cell).ljust(col_widths[i]) for i, cell in enumerate(row)) + " |"
            for row in rows
        ]

        return "\n".join([sep, head_line, sep] + body_lines + [sep])
