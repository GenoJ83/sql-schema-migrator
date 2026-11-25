from typing import Callable, Dict, Any

class HealthChecker:
    def __init__(self):
        self._probes: Dict[str, Callable[[], bool]] = {}

    def register_probe(self, name: str, probe_fn: Callable[[], bool]) -> None:
        self._probes[name] = probe_fn

    def run_check(self) -> Dict[str, Any]:
        results = {}
        all_ok = True
        for name, fn in self._probes.items():
            try:
                ok = fn()
                results[name] = "PASS" if ok else "FAIL"
                if not ok: all_ok = False
            except Exception as e:
                results[name] = f"ERROR: {str(e)}"
                all_ok = False
        return {
            "status": "HEALTHY" if all_ok else "UNHEALTHY",
            "probes": results
        }
