# parser module for VM translator stage 1: stack arithmetic commands

import os
# initialise variables
read_data = []
command_counter = 0
current_command = []


def constructor(infile):
    global read_data

    file_to_write = os.path.basename(infile)

    with open(file_to_write) as input_file:
        for line in input_file:
            write_line = False

            for index, char in enumerate(line):
                if char in ('/', ' '):
                    break

                write_line = True

            if write_line:
                read_data.append(line.rstrip())

    read_data.pop(0)


def has_more_commands():

    # check if reached eof
    if current_command == ' ':
        return False
    else:
        return True


def advance():
    global command_counter
    global current_command
    global read_data

    # if there are more commands to read
    #    store next command in current_command
    if command_counter < len(read_data):
        current_command = read_data[command_counter]
    else:
        current_command = ' '

    command_counter += 1


def command_type():

    if len(current_command) > 0:
        # currently only returns arithmetic or error
        if current_command[0] in {'a', 's', 'n', 'e', 'g', 'l', 'o'}:
            return 'C_ARITHMETIC'
        elif current_command[0] == 'p' and current_command[1] == 'u':
            return 'C_PUSH'
        elif current_command[0] == 'p' and current_command[1] == 'o':
            return 'C_POP'
        else:
            return 'Error: unrecognised command'
    else:
        return 'Error: did no receive command'


def arg1():
    type_of_command = command_type()

    if type_of_command == 'C_ARITHMETIC':
        return current_command
    elif type_of_command == 'C_PUSH':
        # parse line for first argument
        push_arguments = ''
        for i in current_command[5:]:
            if i.isalpha():
                push_arguments = push_arguments + i
        return push_arguments
    elif type_of_command == 'C_POP':
        # parse line for first argument
        pop_arguments = ''
        for i in current_command[4:]:
            if i.isalpha():
                pop_arguments = pop_arguments + i
        return pop_arguments
    else:
        return 'Error: cannot return argument'


def arg2():

    if command_type() == 'C_PUSH':
        argument_2 = ''
        # get value at end of current_command
        for i in current_command:
            if i.isnumeric():
                argument_2 = argument_2 + i
        return int(argument_2)
    elif command_type() == 'C_POP':
        argument_2 = ''
        # get value at end of current_command
        for i in current_command:
            if i.isnumeric():
                argument_2 = argument_2 + i
        return int(argument_2)
    else:
        return 0
