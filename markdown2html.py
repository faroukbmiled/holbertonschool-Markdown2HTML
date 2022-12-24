#!/usr/bin/python3
"""markdown2html.py ,markdown converter"""


import sys


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

    if len(sys.argv) < 3:
        print(
            "Usage: ./markdown2html.py README.md README.html", file=sys.stderr
            )
        sys.exit(1)

    file = sys.argv[1]
    out = sys.argv[2]

    # Convert the markdown to HTML
    md_to_html(file, out)
