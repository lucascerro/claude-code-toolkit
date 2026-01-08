# Claude Code Toolkit

Skills and extensions for [Claude Code](https://docs.anthropic.com/en/docs/claude-code).

## Skills

| Skill | Description |
|-------|-------------|
| [token-counter](skills/token-counter/) | Count tokens using tiktoken (Claude/GPT) or Qwen3 tokenizer |

## Installation

Copy the skill folder to your Claude Code skills directory. See each skill's README for additional setup.

### Global install (all projects)

```bash
git clone https://github.com/lucascerro/claude-code-toolkit.git /tmp/claude-code-toolkit
cp -r /tmp/claude-code-toolkit/skills/token-counter ~/.claude/skills/
rm -rf /tmp/claude-code-toolkit
```

### Project-local install

```bash
git clone https://github.com/lucascerro/claude-code-toolkit.git /tmp/claude-code-toolkit
cp -r /tmp/claude-code-toolkit/skills/token-counter ./.claude/skills/
rm -rf /tmp/claude-code-toolkit
```

## License

MIT
