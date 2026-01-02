# Skill: Task Classifier

## Purpose
Classify task complexity (1-10) to route to optimal model.

## Complexity Matrix

| Score | Complexity | Examples | Recommended Model |
|-------|------------|----------|-------------------|
| 1-2 | Trivial | Typo fix, comment update | MiniMax-lightning |
| 3-4 | Simple | Add field, simple function | MiniMax M2.1 |
| 5-6 | Medium | New API endpoint, refactor | Sonnet → Codex/Gemini |
| 7-8 | High | Multi-file feature, migration | Opus → Sonnet → CLIs |
| 9-10 | Exceptional | Architecture redesign, security fix | Opus (thinking) |

## Classification Criteria

### Technical Factors
- Files affected (1 = trivial, 10+ = exceptional)
- Cross-module dependencies
- Database schema changes
- External API integrations

### Risk Factors
- Security implications (auth, payments, data)
- Breaking change potential
- Rollback difficulty

### Cognitive Factors
- Novel problem (no existing patterns)
- Ambiguity in requirements
- Trade-off decisions required

## Output Format

```json
{
  "complexity": 7,
  "reasoning": "Multi-file feature with database changes and auth integration",
  "recommended_model": "opus",
  "delegation": ["codex:security", "gemini:integration-tests"],
  "estimated_iterations": 12,
  "risk_level": "medium"
}
```

## Model Routing

| Complexity | Primary | Secondary | Fallback |
|------------|---------|-----------|----------|
| 1-2 | MiniMax-lightning | - | - |
| 3-4 | MiniMax M2.1 | - | - |
| 5-6 | Sonnet | Codex/Gemini | MiniMax |
| 7-8 | Opus | Sonnet + CLIs | MiniMax |
| 9-10 | Opus (thinking) | Codex | Gemini |

## Iteration Limits

| Model | Max Iterations |
|-------|----------------|
| Claude (Sonnet/Opus) | 15 |
| MiniMax M2.1 | 30 |
| MiniMax-lightning | 60 |
