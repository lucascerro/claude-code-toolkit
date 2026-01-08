#!~/.claude/skills/token-counter/.venv/bin/python
"""Minimal token counter - tiktoken (default) or Qwen3 tokenizer."""
import sys
import argparse


def count_tiktoken(text, model="cl100k_base"):
    import tiktoken
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        encoding = tiktoken.get_encoding(model)
    return len(encoding.encode(text))


def count_qwen(text):
    import os
    os.environ["TRANSFORMERS_VERBOSITY"] = "error"
    from transformers import AutoTokenizer
    local_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "qwen_tokenizer")
    if os.path.exists(local_path):
        tokenizer = AutoTokenizer.from_pretrained(local_path, local_files_only=True)
    else:
        tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen3-32B")
    return len(tokenizer.encode(text))


def main():
    parser = argparse.ArgumentParser(description="Count tokens in text")
    parser.add_argument("text", nargs="?", help="Text to tokenize (reads stdin if omitted)")
    parser.add_argument("--qwen", action="store_true", help="Use Qwen3 tokenizer instead of tiktoken")
    parser.add_argument("--model", default="cl100k_base", help="tiktoken model/encoding (default: cl100k_base)")
    args = parser.parse_args()

    if args.text:
        text = args.text
    else:
        text = sys.stdin.read()

    if not text:
        print(0)
        return

    count = count_qwen(text) if args.qwen else count_tiktoken(text, args.model)
    print(count)


if __name__ == "__main__":
    main()
