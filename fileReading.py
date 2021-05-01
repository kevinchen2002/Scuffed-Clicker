from pathlib import Path
import os
from functions import *



# read the file
def read_by_line(filename):

    input_file = open(Path("./") / filename)
    lines = input_file.readlines()

    return lines

# determines if all commands and params in the text file are valid
def are_commands_valid(list_of_lines):

    for line in list_of_lines:
        try:
            command = line.split(" ")[0].lower()
            params = line.split(" ")[1]

        # no spaces included
        except:
            return False

        if (command == "click"):

            first_param = params[1: len(params)-2].split(",")[0]
            second_param = params[1: len(params)-2].split(",")[1]

            # if params are proper numbers
            if not(first_param.isnumeric() and second_param.isnumeric()):
                return False
    return True



# reads line and excutes appropiate command
def parse_line(line):
    command = line[0: 5]
    if command == "click":
        params = line.split(" ")[1]
        first_param = params[1: len(params)-2].split(",")[0]
        second_param = params[1: len(params)-2].split(",")[1]
        moveClick(first_param, second_param)
        


lines = read_by_line("input.txt")
if (are_commands_valid(lines)):
    for line in lines:
        parse_line(line)

moveClick(100,100)