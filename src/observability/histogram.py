from typing import List, Dict

class LatencyHistogram:
    def __init__(self, buckets: List[float] = None):
        self.buckets = sorted(buckets or [5.0, 10.0, 25.0, 50.0, 100.0, 250.0, 500.0])
        self.observations: List[float] = []

    def observe(self, val_ms: float) -> None:
        self.observations.append(val_ms)

    def percentile(self, p: float) -> float:
        if not self.observations:
            return 0.0
        sorted_obs = sorted(self.observations)
        idx = int(len(sorted_obs) * (p / 100.0))
        return sorted_obs[min(idx, len(sorted_obs) - 1)]

    def bucket_counts(self) -> Dict[str, int]:
        counts = {f"le_{b}": 0 for b in self.buckets}
        counts["le_inf"] = len(self.observations)
        for val in self.observations:
            for b in self.buckets:
                if val <= b:
                    counts[f"le_{b}"] += 1
        return counts
