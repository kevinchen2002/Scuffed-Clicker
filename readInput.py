from pathlib import Path
import os
from functions import *
import re
import pyautogui

moveFind = re.compile(r"""move\((\d*),(\d*)\)""")


# def are_commands_valid(list_of_lines):


def parse_line(line):
    moveCoordinates = moveFind.search(line)
    print(moveCoordinates.group(1))


parse_line("move(123,51)")
