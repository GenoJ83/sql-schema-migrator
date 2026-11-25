from src.observability.prometheus_exporter import PrometheusExporter

def test_prometheus_formatting():
    c = PrometheusExporter.format_counter("cli_invocations_total", 42, "Total invocations")
    assert "# HELP cli_invocations_total Total invocations" in c
    assert "# TYPE cli_invocations_total counter" in c
    assert "cli_invocations_total 42" in c

    g = PrometheusExporter.format_gauge("memory_resident_mb", 128.5)
    assert "# TYPE memory_resident_mb gauge" in g
    assert "memory_resident_mb 128.5" in g
