#!/usr/bin/python3
"""markdown2html.py ,markdown converter"""

import sys
import os

if __name__ == "__main__":

    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)

    file = sys.argv[1]
    out = sys.argv[2]

    if not os.path.exists(file):
        sys.stderr.write(f"Missing {file}\n")
        exit(1)

    with open(file, "r") as f:
        markdown_string = f.read()

    lines = markdown_string.split("\n")

    converted = []
    lines_count = 0

    for line in lines:

        line = line.strip()

        if line.startswith("#"):
            heading_level = line.count("#")
            heading_text = line.strip("#").strip()

            if lines_count > 0:
                converted.append("</ul>")
                lines_count = 0

            converted.append(
                f"<h{heading_level}>{heading_text}</h{heading_level}>"
                )

        elif line.startswith("-"):
            if lines_count == 0:
                converted.append("<ul>")
            list_first = line.strip("- ")
            list_strip = list_first.rstrip('\n')
            converted.append(f"<li>{list_strip}</li>")
            lines_count += 1

        elif line:
            if lines_count > 0:
                converted.append("</ul>")
                lines_count = 0

            converted.append(f"<p>{line}</p>")

    if lines_count > 0:
        converted.append("</ul>")

    html = "\n".join(converted)

    with open(out, "w") as f:
        f.write(html)

    exit(0)
