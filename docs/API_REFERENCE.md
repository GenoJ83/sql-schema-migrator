# API Reference & Architecture Guide

## Core Subsystems
- **Cascading Configuration**: Multi-tiered configuration resolution with environment overrides.
- **LRU TTL Cache**: In-memory high-throughput cache with millisecond expiration bounds.
- **Resilience Engine**: Exponential backoff retry policies and circuit breakers.
- **Telemetry Counters**: OpenTelemetry metrics integration and Prometheus gauges.
- **Tamper-Evident Audit Chains**: Cryptographic SHA-256 blockchain-style event verification.
