# Claude Code Toolkit

Skills and extensions for [Claude Code](https://docs.anthropic.com/en/docs/claude-code).

## Skills

| Skill | Description | Setup |
|-------|-------------|-------|
| [token-counter](skills/token-counter/) | Count tokens using tiktoken (Claude/GPT) or Qwen3 tokenizer | `uv sync` |

**Setup column:** Most skills work out of the box. If a skill lists setup requirements, see its README for details.

## Installation

Copy the skill folder you want to your Claude Code skills directory:
- Global: `~/.claude/skills/`
- Project-local: `./.claude/skills/`

### Example: Install token-counter globally

```bash
git clone https://github.com/lucascerro/claude-code-toolkit.git /tmp/claude-code-toolkit
cp -r /tmp/claude-code-toolkit/skills/token-counter ~/.claude/skills/
rm -rf /tmp/claude-code-toolkit
```

Then follow any setup instructions in the skill's README.

### Example: Install token-counter in current project

```bash
git clone https://github.com/lucascerro/claude-code-toolkit.git /tmp/claude-code-toolkit
mkdir -p .claude/skills
cp -r /tmp/claude-code-toolkit/skills/token-counter ./.claude/skills/
rm -rf /tmp/claude-code-toolkit
```

## License

MIT
