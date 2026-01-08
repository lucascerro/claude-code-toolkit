# Claude Code Toolkit

Skills and extensions for [Claude Code](https://docs.anthropic.com/en/docs/claude-code).

## Skills

| Skill | Description | Setup |
|-------|-------------|-------|
| [token-counter](skills/token-counter/) | Count tokens using tiktoken (Claude/GPT) or Qwen3 tokenizer | `uv sync` and optional Qwen tokenizer download |

**Setup column:** Some skills have mandatory and/or optional setup requirements, see their README for details.

## Installation

Copy skill folders to your Claude Code skills directory:
- Global: `~/.claude/skills/`
- Project-local: `./.claude/skills/`

### Install all skills globally

```bash
git clone https://github.com/lucascerro/claude-code-toolkit.git /tmp/claude-code-toolkit
cp -r /tmp/claude-code-toolkit/skills/* ~/.claude/skills/
rm -rf /tmp/claude-code-toolkit
```

### Install all skills in current project

```bash
git clone https://github.com/lucascerro/claude-code-toolkit.git /tmp/claude-code-toolkit
mkdir -p .claude/skills
cp -r /tmp/claude-code-toolkit/skills/* ./.claude/skills/
rm -rf /tmp/claude-code-toolkit
```

Then follow any setup instructions in each skill's README.

## License

MIT
