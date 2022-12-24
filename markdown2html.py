#!/usr/bin/python3
"""markdown2html.py ,markdown converter"""


import sys
import os


def md_to_html(file, out):

    with open(file, "r", encoding="utf-8") as f:
        markdown_string = f.read()

    lines = markdown_string.split("\n")

    converted = []

    for line in lines:
        line = line.strip()

        if line.startswith("#"):
            heading_level = line.count("#")
            heading_text = line.strip("#").strip()

            converted.append(
                f"<h{heading_level}>{heading_text}</h{heading_level}>"
                )

        elif line:
            converted.append(f"<p>{line}</p>")

    html = "\n".join(converted)

    with open(out, "w", encoding="utf-8") as f:
        f.write(html)


if __name__ == "__main__":

    file = sys.argv[1]
    out = sys.argv[2]

    if len(sys.argv) < 3:
        sys.stderr.write(
            "Usage: ./markdown2html.py README.md README.html"
            )
        sys.exit(1)

    if not os.path.exists(file):
        sys.stderr.write(f"Missing {file}")
        sys.exit(1)

    md_to_html(file, out)
