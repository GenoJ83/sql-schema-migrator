"""Unit tests for retry policies and chunk streaming."""
import io
from src.resilience.retry_policy import retry_call
from src.io.chunk_streamer import ChunkStreamer

def test_retry_success():
    attempts = 0
    def flaky():
        nonlocal attempts
        attempts += 1
        if attempts < 2:
            raise RuntimeError("Transient error")
        return "SUCCESS"

    result = retry_call(flaky, max_attempts=3, base_delay=0.01)
    assert result == "SUCCESS"
    assert attempts == 2

def test_chunk_streamer():
    streamer = ChunkStreamer(chunk_size=4)
    data = io.BytesIO(b"HelloWorld123")
    chunks = list(streamer.stream_bytes(data))
    assert b"".join(chunks) == b"HelloWorld123"
