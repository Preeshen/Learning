# Promotion Milestones (generated — do not hand-edit; see roadmap.yaml)

## Agent evaluation and observability platform (`agent-eval-observability-platform`)

- **Opens after day**: 36
- **Prerequisite days**: 24, 28, 31, 32, 33, 35
- **Purpose**: Ingest agent traces, score whole trajectories against labelled outcomes, gate releases on regression, and expose the result as a dashboard. Evaluation is the scarcest skill in agentic hiring and the one this learner's existing experience compounds fastest.
- **Demonstrates**:
  - Trajectory scoring against a labelled trace set, not final-answer accuracy
  - Regression gating that distinguishes a real drop from run-to-run variance
  - OpenTelemetry-style tracing with per-step cost and latency attribution
  - Deployed, instrumented and debuggable from logs alone
- **Supports roles**: agentic-ai, test-validation
- **Record**: this project is built in a separate repository; record its pointer in `promoted/README.md`

## Multi-backend inference gateway (`multi-backend-inference-gateway`)

- **Opens after day**: 125
- **Prerequisite days**: 59, 62, 68, 81, 82, 123, 124
- **Purpose**: A service routing requests across a local quantized model and a hosted API, with batching, response caching, rate-limit backoff and health-check fallback when a backend degrades.
- **Demonstrates**:
  - Request batching and response caching under a stated load profile
  - Rate-limit backoff and automatic fallback, measured against a no-fallback baseline
  - Containerised, configurable, and debuggable from logs alone
- **Supports roles**: fde, inference
- **Record**: this project is built in a separate repository; record its pointer in `promoted/README.md`

## Production MCP server with governance (`production-mcp-server`)

- **Opens after day**: 89
- **Prerequisite days**: 52, 53, 54, 56, 61, 88
- **Purpose**: An MCP server for a real domain with scoped permissions, a path jail, resources and prompts, an approval path for side-effecting tools, and an audit trail. Scarce production experience in a young protocol.
- **Demonstrates**:
  - Least-privilege tool scoping with a provable sandbox boundary
  - Resources and prompts, not only tools
  - Audit logging and an approval gate for side-effecting calls
  - Deployed with authentication and monitored
- **Supports roles**: agentic-ai, fde
- **Record**: this project is built in a separate repository; record its pointer in `promoted/README.md`

