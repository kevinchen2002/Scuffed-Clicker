from pathlib import Path
import os
from functions import *
import re
import pyautogui

moveFind = re.compile(r"""move\s\((\d*),(\d*)\)""")
imageFind = re.compile(r"""imageclick\s\((.*?)\)""")
clickFind = re.compile(r"""click\s\((\d*),(\d*)\)""")
writeFind = re.compile(r"""write\s\((.*?)\)""")
delayFind = re.compile(r"""delay\s\((\d*?)\)""")
scollDownFind = re.compile(r"""scrolldown\s\((\d*?)\)""")
scollUpFind = re.compile(r"""scrollup\s\((\d*?)\)""")
typeKeyFind = re.compile(r"""typekey\s\((.*?)\)""")


def are_commands_valid(list_of_lines):
    for line in list_of_lines:
        line.lower()
        if line.startswith("imageclick"):
            check = imageFind.search(line)
            if (check == None):
                return False
            else:
                continue

        elif line.startswith("move"):
            check = moveFind.search(line)
            if (check == None):
                return False
            else:
                continue

        elif line.startswith("clickfind"):
            check = clickFind.search(line)
            if (check == None):
                return False
            else:
                continue

        elif line.startswith("write"):
            check = writeFind.search(line)
            if (check == None):
                return False
            else:
                continue

        elif line.startswith("typekey"):
            check = typeKeyFind.search(line)
            if (check == None):
                return False
            else:
                continue

        elif line.startswith("scrollup"):
            check = typekeyFind.search(line)
            if (check == None):
                return False
            else:
                continue

        elif line.startswith("scrolldown"):
            check = scrolldownFind.search(line)
            if (check == None):
                return False
            else:
                continue

        elif line.startswith("delay"):
            check = delayFind.search(line)
            if (check == None):
                return False
            else:
                continue
    return True
