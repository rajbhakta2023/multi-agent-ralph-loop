---
name: orchestrator
description: "Full orchestration: clarify → classify → delegate → execute → validate → retrospective"
argument-hint: "<task description>"
---

# /orchestrator

Full orchestration with mandatory 6-step flow.

## Usage
```
/orchestrator Implement OAuth2 with Google
/orchestrator Migrate database from MySQL to PostgreSQL
```

## Execution
```
Task("@orchestrator $ARGUMENTS")
```

Equivalent: `ralph orch "task"`
