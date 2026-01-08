---
description: Count tokens in text using tiktoken or Qwen3 tokenizer. Use when estimating API costs or analyzing text length for LLM context windows.
allowed-tools: Bash, Read
---

# Token Counter

Minimal, composable token counter. Pipe any text source into it.

## Script

```bash
~/.claude/skills/token-counter/count_tokens [OPTIONS] [TEXT]
```

**Output:** Just the token count (integer).

## Options

| Flag | Description |
|------|-------------|
| `--qwen` | Use Qwen3 tokenizer (via transformers) instead of tiktoken |
| `--model MODEL` | tiktoken encoding (default: `cl100k_base` for Claude) |

Common `--model` values:
- `cl100k_base` - Claude, GPT-4, GPT-3.5-turbo (default)
- `o200k_base` - GPT-4o
- `p50k_base` - text-davinci-003, Codex

## Usage

The script reads from **stdin** or a **positional argument**. Compose with any command via pipes. Avoid using the Read tool beforehand, as that will just bloat the context window.

### Direct text
```bash
~/.claude/skills/token-counter/count_tokens "Your text here"
```

### From a file
```bash
cat /path/to/file.txt | ~/.claude/skills/token-counter/count_tokens
```

### From multiple files
```bash
cat *.md | ~/.claude/skills/token-counter/count_tokens
```

### From SQLite
```bash
sqlite3 database.db "SELECT content FROM documents" | ~/.claude/skills/token-counter/count_tokens
```

### From JSON (via jq)
```bash
cat data.json | jq -r '.text' | ~/.claude/skills/token-counter/count_tokens
```

### From an API
```bash
curl -s https://api.example.com/content | ~/.claude/skills/token-counter/count_tokens
```

### Using Qwen3 tokenizer
```bash
cat file.txt | ~/.claude/skills/token-counter/count_tokens --qwen
```

### Using GPT-4o encoding
```bash
cat file.txt | ~/.claude/skills/token-counter/count_tokens --model o200k_base
```

## Composability

This script follows Unix philosophy: do one thing, compose via pipes. To count tokens from any data source:

1. Use the appropriate CLI tool to extract/fetch the text (sqlite3, jq, curl, cat, etc.)
2. Pipe the output to this script
3. Receive the token count

The script itself has no knowledge of databases, file formats, or APIs - that logic belongs to the tools you compose it with.
