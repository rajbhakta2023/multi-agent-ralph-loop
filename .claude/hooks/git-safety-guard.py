#!/usr/bin/env python3
"""
git-safety-guard.py - Blocks destructive git and filesystem commands

This hook intercepts Bash commands before execution and blocks potentially
destructive operations that could cause data loss.

Based on: https://github.com/Dicklesworthstone/misc_coding_agent_tips_and_scripts

BLOCKED COMMANDS:
  - git checkout -- <files>     (discards uncommitted changes)
  - git restore <files>         (overwrites working tree)
  - git reset --hard            (destroys uncommitted changes)
  - git reset --merge           (can lose uncommitted changes)
  - git clean -f                (removes untracked files permanently)
  - git push --force / -f       (destroys remote history)
  - git push origin +branch     (force push variant)
  - git branch -D               (force-deletes without merge check)
  - git stash drop              (permanently deletes stash)
  - git stash clear             (deletes ALL stashes)
  - rm -rf (non-temp dirs)      (recursive deletion)

ALLOWED SAFE PATTERNS:
  - git checkout -b <branch>    (creates new branch)
  - git checkout --orphan       (creates orphan branch)
  - git restore --staged        (unstages only)
  - git clean -n / --dry-run    (preview mode)
  - rm -rf /tmp/... or $TMPDIR  (ephemeral directories)

EXIT CODES:
  0 = Allow command (silent)
  Non-zero with JSON = Block command

INSTALLATION:
  User level:  ~/.claude/hooks/git-safety-guard.py
  Project:     .claude/hooks/git-safety-guard.py

  Add to settings.json:
  {
    "hooks": {
      "PreToolUse": [{
        "matcher": "Bash",
        "hooks": [{
          "type": "command",
          "command": "~/.claude/hooks/git-safety-guard.py"
        }]
      }]
    }
  }
"""

import json
import os
import re
import sys

# Patterns that are ALWAYS safe (checked first)
SAFE_PATTERNS = [
    # Git branching (safe)
    r"git\s+checkout\s+(-b|--orphan)\s+",
    r"git\s+switch\s+(-c|--create)\s+",

    # Git restore staged only (doesn't discard working tree)
    r"git\s+restore\s+--staged\s+",

    # Git clean dry-run (preview only)
    r"git\s+clean\s+.*(-n|--dry-run)",

    # rm in temp directories (ephemeral)
    r"rm\s+(-rf|-fr|--recursive)\s+(/tmp/|/var/tmp/|\$TMPDIR/|/private/tmp/)",
    r"rm\s+(-rf|-fr|--recursive)\s+['\"]?/tmp/",
    r"rm\s+(-rf|-fr|--recursive)\s+['\"]?/var/tmp/",

    # Git status/log/diff (read-only)
    r"git\s+(status|log|diff|show|branch|remote|fetch)\b",

    # Git add/commit (safe write operations)
    r"git\s+(add|commit|pull|stash\s+push|stash\s+save)\b",
]

# Patterns that are BLOCKED (destructive)
BLOCKED_PATTERNS = [
    # Discard uncommitted changes
    (r"git\s+checkout\s+--\s+",
     "discards uncommitted changes permanently"),

    # Restore without --staged overwrites working tree
    (r"git\s+restore\s+(?!--staged).*\S+",
     "overwrites working tree changes without stash"),

    # Hard reset destroys changes
    (r"git\s+reset\s+--hard",
     "destroys all uncommitted changes permanently"),

    # Merge reset can lose changes
    (r"git\s+reset\s+--merge",
     "can lose uncommitted changes during merge resolution"),

    # Clean force removes untracked files
    (r"git\s+clean\s+.*-f(?!.*(-n|--dry-run))",
     "removes untracked files permanently (use -n first to preview)"),

    # Force push destroys remote history
    (r"git\s+push\s+.*--force",
     "destroys remote history - coordinate with team first"),
    (r"git\s+push\s+.*-f\b",
     "force push destroys remote history"),
    (r"git\s+push\s+\S+\s+\+",
     "force push via + prefix destroys remote history"),

    # Force delete branch without merge check
    (r"git\s+branch\s+-D\s+",
     "force-deletes branch without checking if merged"),

    # Stash drop/clear permanently deletes
    (r"git\s+stash\s+drop",
     "permanently deletes stashed changes"),
    (r"git\s+stash\s+clear",
     "permanently deletes ALL stashed changes"),

    # Recursive delete outside temp directories
    (r"rm\s+(-rf|-fr|--recursive)\s+(?!/tmp/)(?!/var/tmp/)(?!\$TMPDIR)",
     "recursive deletion outside temp directories - verify path first"),

    # Rebase on shared branches
    (r"git\s+rebase\s+.*\s+(main|master|develop)\b",
     "rebasing shared branches can cause issues for collaborators"),
]


def is_safe_pattern(command: str) -> bool:
    """Check if command matches a known safe pattern."""
    for pattern in SAFE_PATTERNS:
        if re.search(pattern, command, re.IGNORECASE):
            return True
    return False


def check_blocked_pattern(command: str) -> tuple[bool, str]:
    """Check if command matches a blocked pattern. Returns (blocked, reason)."""
    for pattern, reason in BLOCKED_PATTERNS:
        if re.search(pattern, command, re.IGNORECASE):
            return True, reason
    return False, ""


def main():
    try:
        # Read hook input from stdin
        input_data = sys.stdin.read()
        if not input_data.strip():
            sys.exit(0)  # No input, allow

        hook_input = json.loads(input_data)

        # Only process Bash tool calls
        tool_name = hook_input.get("tool_name", "")
        if tool_name != "Bash":
            sys.exit(0)  # Not Bash, allow

        # Extract the command
        tool_input = hook_input.get("tool_input", {})
        command = tool_input.get("command", "")

        if not command:
            sys.exit(0)  # No command, allow

        # Check safe patterns first (always allow)
        if is_safe_pattern(command):
            sys.exit(0)

        # Check blocked patterns
        blocked, reason = check_blocked_pattern(command)

        if blocked:
            # Return denial response
            response = {
                "decision": "block",
                "reason": f"BLOCKED by git-safety-guard: {reason}. "
                         f"Command: {command[:100]}{'...' if len(command) > 100 else ''}. "
                         f"If truly needed, ask the user to run it manually."
            }
            print(json.dumps(response))
            sys.exit(1)

        # Allow by default (silent exit)
        sys.exit(0)

    except json.JSONDecodeError:
        # Invalid JSON input, allow (fail open for usability)
        sys.exit(0)
    except Exception as e:
        # Log error but allow (fail open)
        sys.stderr.write(f"git-safety-guard error: {e}\n")
        sys.exit(0)


if __name__ == "__main__":
    main()
