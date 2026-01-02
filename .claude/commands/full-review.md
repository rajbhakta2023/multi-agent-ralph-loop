---
name: full-review
description: "Multi-model review with 6 parallel subagents"
argument-hint: "<path>"
---

# /full-review

Launch 6 subagents in parallel:
- Codex Security
- Codex Bugs  
- Codex Unit Tests
- Gemini Integration
- Gemini Research
- MiniMax Second Opinion

## Usage
```
/full-review src/
```

## Execution
```bash
ralph parallel "$ARGUMENTS"
```
