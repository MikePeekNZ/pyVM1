# parser module for VM translator stage 1: stack arithmetic commands

# initialise variables
read_data = []
command_counter = 0
current_command = []


def constructor(infile):

    # hold contents of .vm files
    global read_data

    with open(infile) as input_file:
        for line in input_file:
            line_to_copy = ''

            write_line = False

            # ignore comments and empty lines
            for index, char in enumerate(line):
                if char in ('/', ' '):
                    break

                write_line = True

            if write_line:
                for i in range(1, len(line)):
                    if (line[i] == ' ' and line[i - 1] == ' ') \
                            or line[i] == '/':
                        line_to_copy = line[0:i]
                        break
                if len(line_to_copy) == 0:
                    line_to_copy = line

                read_data.append(line_to_copy.rstrip())

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
        if current_command[0] in {'a', 's', 'n', 'e', 'o'} or\
                (current_command[0] == 'g' and current_command[1] == 't') or\
                (current_command[0] == 'l' and current_command[1] == 't'):
            return 'C_ARITHMETIC'
        elif current_command[0] == 'p' and current_command[1] == 'u':
            return 'C_PUSH'
        elif current_command[0] == 'p' and current_command[1] == 'o':
            return 'C_POP'
        elif current_command[0] == 'l' and current_command[1] == 'a':
            return 'C_LABEL'
        elif current_command[0] == 'g' and current_command[1] == 'o':
            return 'C_GOTO'
        elif current_command[0] == 'i':
            return 'C_IF'
        else:
            return 'Error: unrecognised command'
    else:
        return 'Error: did not receive command'


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
    elif type_of_command == 'C_LABEL':
        label_argument = ''
        for i in current_command[6:]:
            label_argument = label_argument + i
        return label_argument
    elif type_of_command == 'C_GOTO':
        goto_argument = ''
        for i in current_command[5:]:
            goto_argument = goto_argument + i
        return goto_argument
    elif type_of_command == 'C_IF':
        if_argument = ''
        for i in current_command[8:]:
            if_argument = if_argument + i
        return if_argument
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
