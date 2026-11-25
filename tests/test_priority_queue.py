import pytest
from src.concurrency.priority_queue import BoundedPriorityQueue

def test_bounded_priority_queue():
    pq = BoundedPriorityQueue(maxsize=3)
    assert pq.push("task_low", priority=50) is True
    assert pq.push("task_critical", priority=1) is True
    assert pq.push("task_normal", priority=10) is True
    assert pq.push("task_overflow", priority=5) is False

    assert pq.pop() == "task_critical"
    assert pq.pop() == "task_normal"
    assert pq.pop() == "task_low"
