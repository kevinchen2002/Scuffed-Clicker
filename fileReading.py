from pathlib import Path
import os

def read_by_line(filename):
    input_file = open(Path("./") / filename)
    lines = input_file.readlines()
    return lines