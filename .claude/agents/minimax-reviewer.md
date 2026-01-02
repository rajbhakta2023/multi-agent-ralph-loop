---
name: minimax-reviewer
description: "Universal fallback reviewer using MiniMax M2.1 (~8% cost of Claude)."
tools: Bash, Read
model: sonnet
---

# 💰 MiniMax Reviewer (Universal Fallback)

## Use Cases

- Second opinion on any task
- Extended loops (30-60 iterations vs Claude's 15)
- Cost-effective validation
- Parallel review alongside other models

## Invocation

### Standard Query
```bash
mmc --query "Review/analyze: $TASK" > /tmp/minimax_result.json 2>&1
```

### Extended Loop
```bash
mmc --loop 30 "$TASK"  # M2.1: 30 iterations
mmc --lightning --loop 60 "$TASK"  # Lightning: 60 iterations
```

### Second Opinion
```bash
mmc --second-opinion "$PREVIOUS_RESULT"
```

## Cost Comparison

| Model | Cost | Max Iterations |
|-------|------|----------------|
| Claude Sonnet | $3/$15 M | 15 |
| MiniMax M2.1 | $0.30/$1.20 M | 30 |
| MiniMax-lightning | $0.15/$0.60 M | 60 |
