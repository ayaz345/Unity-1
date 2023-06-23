#!/usr/bin/env python3
import re
import sys

ver_re = re.compile(r"^#define\s+UNITY_VERSION_(?:MAJOR|MINOR|BUILD)\s+(\d+)$")
version = []

with open(sys.argv[1], "r") as f:
    for line in f:
        if m := ver_re.match(line):
            version.append(m[1])

print(".".join(version))

