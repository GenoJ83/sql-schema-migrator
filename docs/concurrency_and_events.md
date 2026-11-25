# Concurrency, Priority Queues & Event Processing

## Architecture
The concurrency subsystem provides resilient task execution utilities for distributed jobs and CLI workflows:
- **PriorityEventBus**: Decoupled pub/sub with Unix-style pattern matching.
- **BoundedPriorityQueue**: Memory-safe task queues with backpressure eviction prevention.
- **TaskWorkerPool**: Uniform execution harness across heterogeneous workloads.
- **DeadLetterQueue**: Retry scheduling with exponential backoff and error tracking.
