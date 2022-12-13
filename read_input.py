"""
Take file as input, read into array of lines (cleaned!).
"""

from pathlib import Path


def read_input(filepath):
    p = Path(filepath)
    print(p.resolve())
    with open(p) as f:
        lines = f.readlines()
        clean_lines = [line.rstrip() for line in lines]
        # print(cleanLines)
    f.close()
    return clean_lines
