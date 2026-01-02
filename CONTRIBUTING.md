# Contributing to Multi-Agent Ralph Wiggum

First off, thanks for taking the time to contribute! This project aims to make AI-assisted development more powerful through multi-agent orchestration.

## Code of Conduct

Be respectful, inclusive, and constructive. We're all here to make something cool.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates.

**Great Bug Reports include:**
- A clear, descriptive title
- Steps to reproduce the behavior
- Expected behavior vs actual behavior
- Your environment (OS, Claude Code version, shell)
- Relevant logs or screenshots

Use the bug report template when creating an issue.

### Suggesting Enhancements

We love new ideas! Enhancement suggestions are tracked as GitHub issues.

**Great Enhancement Suggestions include:**
- A clear, descriptive title
- Step-by-step description of the suggested enhancement
- Explanation of why this would be useful
- Examples of how it would work

### Pull Requests

1. **Fork the repo** and create your branch from `main`
2. **Follow the existing code style** - bash scripts should pass shellcheck
3. **Test your changes** - run the test suite with `bats tests/`
4. **Update documentation** - if you change functionality, update CLAUDE.md and README.md
5. **Write a good commit message** - follow conventional commits format

## Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/multi-agent-ralph-loop.git
cd multi-agent-ralph-loop

# Install locally for testing
./install.sh

# Run tests
bats tests/

# Check bash scripts
shellcheck scripts/ralph scripts/mmc install.sh uninstall.sh
```

## Project Structure

```
multi-agent-ralph-loop/
├── .claude/
│   ├── agents/          # Agent definitions (orchestrator, etc.)
│   ├── commands/        # Slash commands (/clarify, /gates, etc.)
│   ├── hooks/           # Git safety guard, quality gates
│   └── skills/          # Reusable skills (deep-clarification, etc.)
├── scripts/
│   ├── ralph            # Main CLI tool
│   └── mmc              # MiniMax wrapper
├── tests/               # Bats test files
├── install.sh           # Global installer
├── uninstall.sh         # Uninstaller
├── CLAUDE.md            # Claude Code instructions
└── README.md            # Documentation
```

## Contribution Areas

### High Priority
- **New Quality Gates**: Add support for more languages/frameworks
- **Agent Improvements**: Better prompts, new specialized agents
- **MCP Integrations**: Connect to more tools and services
- **Documentation**: Examples, tutorials, use cases

### Medium Priority
- **Performance**: Faster execution, better parallelization
- **Testing**: More test coverage, edge cases
- **Error Handling**: Better error messages, recovery

### Ideas Welcome
- **New Commands**: What would make your workflow better?
- **Integrations**: What tools should Ralph work with?
- **UI/UX**: How can we make the CLI more intuitive?

## Commit Message Format

We use [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation only
- `style`: Formatting, no code change
- `refactor`: Code change that neither fixes a bug nor adds a feature
- `test`: Adding or fixing tests
- `chore`: Maintenance tasks

**Examples:**
```
feat(agents): Add new database-optimizer agent
fix(gates): Handle Python virtual environments correctly
docs(readme): Add troubleshooting section
```

## Testing

All changes should include tests where applicable:

```bash
# Run all tests
bats tests/

# Run specific test file
bats tests/test_ralph_security.bats

# Run with verbose output
bats -v tests/
```

## Review Process

1. **Automated checks** - Tests must pass, shellcheck must be clean
2. **Code review** - At least one maintainer will review your PR
3. **Discussion** - We may ask questions or suggest changes
4. **Merge** - Once approved, we'll merge your contribution!

## Recognition

Contributors will be recognized in:
- The README.md contributors section
- Release notes for significant contributions
- Our eternal gratitude

## Questions?

- Open an issue with the `question` label
- Check existing issues and discussions

## License

By contributing, you agree that your contributions will be licensed under the BSL 1.1 license (converting to Apache 2.0 on 2030-01-01).

---

Thank you for helping make Multi-Agent Ralph Wiggum better!
