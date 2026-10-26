/**
 * Core TypeScript definitions and interface declarations
 */
export interface DiagnosticReport {
  timestamp: number;
  status: 'healthy' | 'degraded' | 'failing';
  metrics: Record<string, number>;
}

export interface ConfigurationOptions {
  timeoutMs?: number;
  maxRetries?: number;
  debugMode?: boolean;
}

export interface ExecutionResult<T = unknown> {
  success: boolean;
  data?: T;
  error?: string;
  durationMs: number;
}
