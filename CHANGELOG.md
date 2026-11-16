# Changelog

## [1.2.0] - 2026-11-16
### Added
- Pluggable extension hook manager (`src/plugins/plugin_manager.py`)
- Thread-safe LRU Cache with TTL timestamp eviction (`src/cache/lru_ttl_cache.py`)
- Prometheus and OpenTelemetry telemetry counters (`src/metrics/telemetry_counters.py`)
- Structured JSON log formatter with correlation IDs (`src/logging/structured_json_logger.py`)
- Cryptographically secure nonce & token generators (`src/security/crypto_tokens.py`)
- Resilient exponential backoff retry policy (`src/resilience/retry_policy.py`)
- Tamper-evident rolling SHA-256 audit log chains (`src/audit/rolling_hash_chain.py`)
- Multi-format serialization for NDJSON, CSV, and XML (`src/serialization/multi_format_exporter.py`)
- Full test coverage for caching, streaming, and resilience subsystems
