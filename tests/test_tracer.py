from src.observability.tracer import TraceSpan

def test_trace_span():
    span = TraceSpan("disk_read")
    span.set_attribute("bytes", 2048)
    assert span.attributes["bytes"] == 2048
    assert span.w3c_traceparent().startswith("00-")
    duration = span.finish()
    assert duration >= 0.0
    assert span.duration_ms == duration
