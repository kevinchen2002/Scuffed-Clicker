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
    
    command = line[0: 10].lower()
    if command == "imageclick":
        print(command)
        param = line.split(" ")[1]
        param = param[1:len(param)-2]
        print(param)
        imageClick(param)

    command = line[0: 5].lower()
    if command == "click":
        print(command)
        params = line.split(" ")[1]
        first_param = params[1: len(params)-2].split(",")[0]
        second_param = params[1: len(params)-2].split(",")[1]
        print(first_param)
        print(second_param)
        moveClick(int(first_param), int(second_param))

    command = line[0: 4].lower()
    if command == "move":
        print(command)
        params = line.split(" ")[1]
        first_param = params[1: len(params)-1].split(",")[0]
        second_param = params[1: len(params)-2].split(",")[1]
        print(first_param)
        print(second_param)
        move(int(first_param), int(second_param))

    command = line[0: 5].lower()
    if command == "write":
        print(command)
        param = line.split(" ")[1]
        param = param[1: len(param)-2]
        write(param)

    command = line[0: 7].lower()
    if command == "typekey":
        print(command)
        param = line.split(" ")[1]
        param = param[1: len(param)-2]
        print(param)
        typeKey(param)

    command = line[0: 8].lower()
    if command == "scrollup":
        print(command)
        param = line.split(" ")[1]
        param = param[1: len(param)-1]
        typeKey(param)   

    command = line[0: 10].lower()
    if command == "scrolldown":
        print(command)
        param = line.split(" ")[1]
        param = param[1: len(param)-1]
        typeKey(param)

    command = line[0: 5].lower()
    if command == "delay":
        print(command)
        param = line.split(" ")[1]
        param = param[1: len(param)-1]
        write(param)



lines = read_by_line("input.txt")
if are_commands_valid(lines):
    for line in lines:
        time.sleep(1)
        parse_line(line)

print("done")
