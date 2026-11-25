from src.concurrency.worker_pool import TaskWorkerPool

def test_task_worker_pool():
    pool = TaskWorkerPool(concurrency=2)
    items = [2, 4, "invalid", 8]
    def square_fn(x):
        if not isinstance(x, (int, float)):
            raise TypeError("Value must be numeric")
        return x * x

    results = pool.execute_batch(square_fn, items)
    assert len(results) == 4
    assert results[0]["status"] == "SUCCESS" and results[0]["result"] == 4
    assert results[2]["status"] == "FAILURE"
    assert pool.throughput_summary()["tasks_executed"] == 4
