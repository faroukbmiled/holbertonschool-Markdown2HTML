#!/usr/bin/python3
"""markdown2html.py, markdown converter"""

import sys
import os
import re

if __name__ == "__main__":

    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)

    file = sys.argv[1]
    out = sys.argv[2]
    bold_re = r"\*\*(.+?)\*\*"
    italic_re = r"__(.+?)__"

    if not os.path.exists(file):
        sys.stderr.write(f"Missing {file}\n")
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
            list_first = line.strip("- ").rstrip("\n")
            list_first = \
                list_first = re.sub(bold_re, r"<b>\1</b>", list_first)
            list_first = \
                list_first = re.sub(italic_re, r"<em>\1</em>", list_first)
            converted.append(f"<li>{list_first}</li>")

        elif line.startswith("* "):
            if not ol_open:
                converted.append("<ol>")
                ol_open = True
            if p_open:
                converted.append("</p>")
                p_open = False
            if ul_open:
                converted.append("</ul>")
                ul_open = False
            list_first = line.strip("* ").rstrip('\n')
            list_first = \
                list_first = re.sub(bold_re, r"<b>\1</b>", html.escape(list_first))
            list_first = \
                list_first = re.sub(italic_re, r"<em>\1</em>", list_first)
            converted.append(f"<li>{list_first}</li>")

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

            line = re.sub(bold_re, r"<b>\1</b>", line)

            line = re.sub(italic_re, r"<em>\1</em>", line)

            converted.append(f"{line}")

        elif not line:
            if p_open:
                p_open = False
                p_counter = 0
                converted.append("</p>")
            if ul_open and list == 0:
                ul_open = False
                converted.append("</ul>")
            if ol_open and list == 0:
                ol_open = False
                converted.append("</ol>")

    if p_open:
        converted.append("</p>")
    if ul_open:
        converted.append("</ul>")
    if ol_open:
        converted.append("</ol>")

    with open(out, "w") as f:
        f.write("\n".join(converted))

    exit(0)
