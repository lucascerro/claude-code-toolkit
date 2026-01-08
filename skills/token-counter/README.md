# Token Counter

Minimal, composable token counter for Claude Code. Supports tiktoken (Claude/GPT) and Qwen3 tokenizers.

## Installation

Requires [uv](https://docs.astral.sh/uv/).

**Note:** This skill requires Python packages (~150MB for venv). The optional Qwen tokenizer adds ~16MB.

### Global install (all projects)

```bash
git clone https://github.com/lucascerro/claude-code-toolkit.git /tmp/claude-code-toolkit
cp -r /tmp/claude-code-toolkit/skills/token-counter ~/.claude/skills/
rm -rf /tmp/claude-code-toolkit
cd ~/.claude/skills/token-counter && uv sync
```

### Project-local install

```bash
git clone https://github.com/lucascerro/claude-code-toolkit.git /tmp/claude-code-toolkit
mkdir -p .claude/skills
cp -r /tmp/claude-code-toolkit/skills/token-counter ./.claude/skills/
rm -rf /tmp/claude-code-toolkit
cd .claude/skills/token-counter && uv sync
```

### Optional: Download Qwen3 tokenizer for offline use

*The `--qwen` flag works without this (downloads on first use)*, but if you want to preemptively download the Qwen tokenizer:

```bash
cd ~/.claude/skills/token-counter
uv run python -c "
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained('Qwen/Qwen3-32B')
tokenizer.save_pretrained('./qwen_tokenizer')
"
```

## Usage

More detailed examples of usage can be found in the [SKILL.md](SKILL.md) file (this was made to be used by Claude Code, as a skill), but here are some examples

```bash
# Direct text
~/.claude/skills/token-counter/count_tokens "Your text here"

# From file
cat file.txt | ~/.claude/skills/token-counter/count_tokens

# Using Qwen3 tokenizer
~/.claude/skills/token-counter/count_tokens --qwen "text"

# Using GPT-4o encoding
~/.claude/skills/token-counter/count_tokens --model o200k_base "text"
```

## Options

| Flag | Description |
|------|-------------|
| `--qwen` | Use Qwen3 tokenizer instead of tiktoken |
| `--model MODEL` | tiktoken encoding (default: `cl100k_base`) |

## Claude Code Skill

This is a [Claude Code skill](https://docs.anthropic.com/en/docs/claude-code). Once installed, Claude Code can use it to count tokens in any text source via pipes.
