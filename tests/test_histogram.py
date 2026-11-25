from src.observability.histogram import LatencyHistogram

def test_histogram_percentiles():
    hist = LatencyHistogram([10.0, 50.0, 100.0])
    for val in [5.0, 12.0, 45.0, 80.0, 150.0]:
        hist.observe(val)

    assert hist.percentile(50) == 45.0
    buckets = hist.bucket_counts()
    assert buckets["le_10.0"] == 1
    assert buckets["le_50.0"] == 3
    assert buckets["le_inf"] == 5
