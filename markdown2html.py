#!/usr/bin/python3
"""markdown2html.py ,markdown converter"""

import sys
from markdown import markdown
import os


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)

    file = sys.argv[1]
    out = sys.argv[2]

    if not os.path.exists(file):
        sys.stderr.write(f"Missing {file}" + "\n")
        exit(1)

    with open(file) as f:
        markdown_text = f.read()
    html_text = markdown(markdown_text)

    with open(out, "w") as f:
        f.write(html_text)

    exit(0)
