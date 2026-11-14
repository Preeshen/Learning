# Promotion Milestones (generated — do not hand-edit; see roadmap.yaml)

## Code review triage agent (`code-review-triage-agent`)

- **Opens after day**: 35
- **Prerequisite days**: 22, 24, 28, 31, 34
- **Purpose**: An agent that ingests a PR diff and triages it (blocking / nitpick / false positive) by running tools — linter, test runner, static analyzer — in a loop, evaluated against a labeled set of real PRs rather than demoed on the happy path.
- **Demonstrates**:
  - Multi-step tool orchestration with malformed/failing tool-call recovery
  - An evaluation set of labeled PRs scored for precision/recall against a no-agent baseline
  - Cost and latency instrumented per review
- **Supports roles**: agentic-ai, fde
- **Record**: this project is built in a separate repository; record its pointer in `promoted/README.md`

## Multi-backend inference gateway (`inference-gateway`)

- **Opens after day**: 49
- **Prerequisite days**: 38, 41, 44, 47
- **Purpose**: A FastAPI service routing requests across 2+ model backends (e.g. a local quantized model and a hosted API), with batching, response caching, rate-limit backoff, and a health-check/fallback path when a backend degrades.
- **Demonstrates**:
  - Request batching and response caching under a stated load profile
  - Rate-limit backoff and automatic fallback to a healthy backend, measured against a no-fallback baseline
  - Deployment-pattern fluency: containerized, configurable, debuggable from logs alone
- **Supports roles**: fde, inference
- **Record**: this project is built in a separate repository; record its pointer in `promoted/README.md`

## Model compression and validation benchmark suite (`compression-validation-suite`)

- **Opens after day**: 63
- **Prerequisite days**: 52, 55, 58, 61
- **Purpose**: Train or fine-tune a small model, then quantize/prune it, reporting accuracy, latency, and memory before vs. after against a stated baseline, plus a systematic adversarial/edge-case test suite rather than a single happy-path accuracy number.
- **Demonstrates**:
  - Classical ML training and evaluation with a reported metric, dataset split, and baseline
  - Inference latency and memory measured before/after compression against the baseline
  - Model size reduction with the accuracy/latency/memory tradeoff reported, not just claimed
  - A systematic test/validation suite covering adversarial and edge-case inputs
- **Supports roles**: ml-engineer, inference, embedded-ml, test-validation
- **Record**: this project is built in a separate repository; record its pointer in `promoted/README.md`

