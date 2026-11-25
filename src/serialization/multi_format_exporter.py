"""Multi-format dictionary and tabular serializer."""
import json
import csv
import io
from typing import List, Dict, Any

class MultiFormatExporter:
    @staticmethod
    def to_ndjson(records: List[Dict[str, Any]]) -> str:
        return "\n".join(json.dumps(r) for r in records) + "\n"

    @staticmethod
    def to_csv(records: List[Dict[str, Any]]) -> str:
        if not records:
            return ""
        out = io.StringIO()
        writer = csv.DictWriter(out, fieldnames=list(records[0].keys()))
        writer.writeheader()
        writer.writerows(records)
        return out.getvalue()
