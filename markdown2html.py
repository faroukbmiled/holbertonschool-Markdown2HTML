#!/usr/bin/python3
"""markdown2html.py ,markdown converter"""

import sys
import os

if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html\n", file=sys.stderr)
        exit(1)

    file = sys.argv[1]
    out = sys.argv[2]

    if not os.path.exists(file):
        print(f"Missing {file}\n", file=sys.stderr)
        exit(1)

    with open(file, "r") as f:
        markdown_string = f.read()

    lines = markdown_string.split("\n")

    converted = []
    ul_open = False
    ol_open = False
    p_open = False
    p_counter = 0

    for line in lines:

        line = line.strip()

        if line.startswith("#"):
            heading_level = line.count("#")
            heading_text = line.strip("#").strip()

            if ul_open:
                converted.append("</ul>")
                ul_open = False
            if ol_open:
                converted.append("</ol>")
                ol_open = False
            if p_open:
                converted.append("</p>")
                p_open = False

            converted.append(
                f"<h{heading_level}>{heading_text}</h{heading_level}>"
            )

        elif line.startswith("-"):
            if not ul_open:
                converted.append("<ul>")
                ul_open = True
            if p_open:
                converted.append("</p>")
                p_open = False
            if ol_open:
                converted.append("</ol>")
                ol_open = False
            list_first = line.strip("- ")
            list_strip = list_first.rstrip('\n')
            converted.append(f"<li>{list_strip}</li>")

        elif line.startswith("*"):
            if not ol_open:
                converted.append("<ol>")
                ol_open = True
            if p_open:
                converted.append("</p>")
                p_open = False
            if ul_open:
                converted.append("</ul>")
                ul_open = False
            list_first = line.strip("* ")
            list_strip = list_first.rstrip('\n')
            converted.append(f"<li>{list_strip}</li>")

        elif line:
            if ul_open:
                converted.append("</ul>")
                ul_open = False
            if ol_open:
                converted.append("</ol>")
                ol_open = False
            if not p_open:
                converted.append("<p>")
                p_counter += 1
                p_open = True

            if p_counter > 1:
                converted.append("<br/>")
            p_counter += 1

            converted.append(f"{line}")

        elif not line:
            if ul_open:
                converted.append("</ul>")
                ul_open = False
            if ol_open:
                converted.append("</ol>")
                ol_open = False
            if p_open:
                converted.append("</p>")
                p_open = False
            p_counter = 0

    if ul_open:
        converted.append("</ul>")
    if ol_open:
        converted.append("</ol>")
    if p_open:
        converted.append("</p>")

    html = "\n".join(converted)

    with open(out, "w") as f:
        f.write(html)

    exit(0)
