"""Automated micro-benchmark runner."""
import time

def benchmark_function(fn, iterations: int = 100):
    start = time.perf_counter()
    for _ in range(iterations):
        fn()
    elapsed = time.perf_counter() - start
    return {
        "iterations": iterations,
        "total_seconds": round(elapsed, 4),
        "ops_per_second": round(iterations / (elapsed + 1e-8), 2)
    }

if __name__ == "__main__":
    res = benchmark_function(lambda: sum(range(1000)), 500)
    print("Benchmark Results:", res)
