"""Unit tests for benchmark suite."""
from benchmarks.benchmark_suite import benchmark_function

def test_benchmark_runner():
    res = benchmark_function(lambda: 1 + 1, iterations=50)
    assert res["iterations"] == 50
    assert res["total_seconds"] >= 0.0
    assert res["ops_per_second"] > 0
