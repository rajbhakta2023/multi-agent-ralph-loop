# Codex CLI Instructions

## Overview
Configuration for Codex CLI (gpt-5.2-codex) as subagent in Ralph Wiggum system.

## Available Skills

Use skills with: `codex exec --yolo --enable-skills -m gpt-5.2-codex "Use [skill-name] skill. [prompt]"`

### Skills
- `security-review` - Security vulnerability analysis
- `bug-hunter` - Deep bug detection
- `test-generation` - Unit test creation
- `ask-questions-if-underspecified` - Clarification before complex tasks

## Invocation Patterns

### Security Review
```bash
codex exec --yolo --enable-skills -m gpt-5.2-codex \
  "Use security-review skill. Analyze: $FILES" \
  > output.json 2>&1
```

### Bug Hunting
```bash
codex exec --yolo --enable-skills -m gpt-5.2-codex \
  "Use bug-hunter skill. Find bugs in: $FILES" \
  > output.json 2>&1
```

### With Clarification
```bash
codex exec --yolo --enable-skills -m gpt-5.2-codex \
  "Use ask-questions-if-underspecified skill. 
   Task: $TASK
   If clear, proceed. If not, ask MUST_HAVE questions." \
  > output.json 2>&1
```

## Output Format
Always request JSON output for parsing:
```json
{
  "status": "success|needs_clarification|error",
  "findings": [],
  "questions": [],
  "summary": ""
}
```

## Integration with Ralph
- Called by Sonnet subagents via bash
- Results parsed and aggregated by orchestrator
- Part of adversarial validation (2/3 consensus)

## Iteration Limits
- Max 15 iterations per invocation (matches Claude limit)
- For extended work, use MiniMax (30/60 iterations)
