#!/usr/bin/env python
import sys
from markdown import markdown
import os

if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    sys.exit(1)

file = sys.argv[1]
out = sys.argv[2]

if not os.path.exists(file):
    print(f"Missing {file}", file=sys.stderr)
    sys.exit(1)

with open(file) as f:
        markdown_text = f.read()
html_text = markdown(markdown_text)

with open(out, "w") as f:
    f.write(html_text)

sys.exit(0)
