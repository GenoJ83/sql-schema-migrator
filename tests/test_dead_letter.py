from src.concurrency.dead_letter import DeadLetterQueue

def test_dead_letter_queue():
    dlq = DeadLetterQueue(max_retries=3, base_delay=0.5)
    assert dlq.record_failure("t-1", {"job": "sync"}, "Connection reset", attempt=1) is True
    assert dlq.record_failure("t-1", {"job": "sync"}, "Connection reset", attempt=2) is True
    assert dlq.record_failure("t-1", {"job": "sync"}, "Connection reset", attempt=3) is False
    assert len(dlq.failures) == 3
    assert dlq.failures[0]["backoff_seconds"] == 0.5
    assert dlq.failures[1]["backoff_seconds"] == 1.0
