# codewriter module for VM translator stage 1: stack arithmetic commands

import os

output_file_data = {}
input_file_name = ''
output_file_name = ''
equal_counter = 0
not_equal_counter = 0
less_than_counter = 0
not_less_than_counter = 0
greater_than_counter = 0
not_greater_than_counter = 0
push_counter = 0


def set_file_name(filename):
    global output_file_data
    global input_file_name

    # flag to show whether processing single file or batch of files
    is_batch_file = True

    # check if processing a batch of files
    if filename[len(filename) - 3] == '.':
        is_batch_file = False

    norm_filename = ''

    # remove .vm extension
    filename_split = os.path.splitext(filename)

    filename_no_extension = filename_split[0]

    # step through char by char switching \ for /
    for i in range(0, len(filename_no_extension)):
        if filename_no_extension[i] == '\\':
            norm_filename = norm_filename + '/'
        else:
            norm_filename = norm_filename + filename[i]

    # add new extension
    if is_batch_file:
        norm_filename = norm_filename + '/batchFilesOut.asm'
    else:
        norm_filename = norm_filename + '.asm'

    # Opens the output file/stream and gets ready to write into it
    output_file_data = open(norm_filename, 'w', encoding='utf-8')

    # copy current filename for static segment
    input_file_name = os.path.basename(filename_no_extension) + '.'


def write_arithmetic(command):
    global output_file_data
    global equal_counter
    global not_equal_counter
    global less_than_counter
    global not_less_than_counter
    global greater_than_counter
    global not_greater_than_counter
    global push_counter

    # Writes the assembly code that is the translation of the given
    # arithmetic command
    if command == 'add':

        # pop local 0
        write_push_pop('C_POP', 'temp', 0)

        # pop local 1
        write_push_pop('C_POP', 'temp', 1)

        # add
        # # store temp 0 in D
        output_file_data.write('@5\n')
        output_file_data.write('D=M\n')

        # # Add D to temp 1
        output_file_data.write('A=A+1\n')
        output_file_data.write('D=D+M\n')

        # # store result of previous calculation in D
        output_file_data.write('@5\n')
        output_file_data.write('M=D\n')

        write_push_pop('C_PUSH', 'temp', 0)
    elif command == 'sub':

        # pop local 0
        write_push_pop('C_POP', 'temp', 0)

        # pop local 1
        write_push_pop('C_POP', 'temp', 1)

        # sub
        # # store temp 0 in D
        output_file_data.write('@5\n')
        output_file_data.write('D=M\n')

        # # sub D from temp 1
        output_file_data.write('A=A+1\n')
        output_file_data.write('D=M-D\n')

        # # store result of previous calculation in D
        output_file_data.write('@5\n')
        output_file_data.write('M=D\n')

        write_push_pop('C_PUSH', 'temp', 0)
    elif command == 'neg':
        # pop local 0
        # # store top of stack in D
        output_file_data.write('@SP\n')
        output_file_data.write('M=M-1\n')
        output_file_data.write('A=M\n')
        # neg
        output_file_data.write('M=-M\n')
        # neg

        # # store result of previous calculation in D
        output_file_data.write('D=M\n')

        # push temp 0

        # # store result of previous calculation in D
        output_file_data.write('@5\n')
        output_file_data.write('M=D\n')

        write_push_pop('C_PUSH', 'temp', 0)
    elif command == 'eq':

        # pop local 0
        write_push_pop('C_POP', 'temp', 0)

        # pop local 1
        write_push_pop('C_POP', 'temp', 1)

        # eq
        # # store temp 0 in D
        output_file_data.write('@5\n')
        output_file_data.write('D=M\n')

        # # sub local 1 from D
        output_file_data.write('A=A+1\n')
        output_file_data.write('D=D-M\n')

        # if D = 0 goto equal
        output_file_data.write('@EQUAL_{}\n'.format(equal_counter))
        output_file_data.write('D;JEQ\n')

        # if D != 0 goto unequal
        output_file_data.write('@NOT_EQUAL_{}\n'.format(not_equal_counter))
        output_file_data.write('D;JNE\n')

        # equal function
        output_file_data.write('(EQUAL_{})\n'.format(equal_counter))
        equal_counter += 1
        output_file_data.write('D=-1\n')
        output_file_data.write('@PUSH_{}\n'.format(push_counter))
        output_file_data.write('0;JMP\n')

        # unequal function
        output_file_data.write('(NOT_EQUAL_{})\n'.format(not_equal_counter))
        not_equal_counter += 1
        output_file_data.write('D=0\n')
        output_file_data.write('@PUSH_{}\n'.format(push_counter))
        output_file_data.write('0;JMP\n')

        # push temp 0

        output_file_data.write('(PUSH_{})\n'.format(push_counter))

        # store D in temp 0
        output_file_data.write('@5\n')
        output_file_data.write('M=D\n')

        push_counter += 1
        write_push_pop('C_PUSH', 'temp', 0)
    elif command == 'gt':

        # pop temp 0
        write_push_pop('C_POP', 'temp', 0)

        # pop temp 1
        write_push_pop('C_POP', 'temp', 1)

        # gt
        # # store temp 1 in D
        output_file_data.write('@5\n')
        output_file_data.write('A=A+1\n')
        output_file_data.write('D=M\n')

        # # sub temp 0 from D
        output_file_data.write('A=A-1\n')
        output_file_data.write('D=D-M\n')

        # if D = 0 goto greater
        output_file_data.write('@GREATER_{}\n'.format(greater_than_counter))
        output_file_data.write('D;JGT\n')

        # if D != 0 goto not_greater
        output_file_data.write('@NOT_GREATER_{}\n'.format(not_greater_than_counter))
        output_file_data.write('D;JLE\n')

        # greater function
        output_file_data.write('(GREATER_{})\n'.format(greater_than_counter))
        greater_than_counter += 1
        output_file_data.write('D=-1\n')
        output_file_data.write('@PUSH_{}\n'.format(push_counter))
        output_file_data.write('0;JMP\n')

        # not_greater function
        output_file_data.write('(NOT_GREATER_{})\n'.format(not_greater_than_counter))
        not_greater_than_counter += 1
        output_file_data.write('D=0\n')
        output_file_data.write('@PUSH_{}\n'.format(push_counter))
        output_file_data.write('0;JMP\n')

        # push temp 0

        output_file_data.write('(PUSH_{})\n'.format(push_counter))

        # store D in temp 0
        output_file_data.write('@5\n')
        output_file_data.write('M=D\n')

        push_counter += 1
        write_push_pop('C_PUSH', 'temp', 0)
    elif command == 'lt':

        # pop local 0
        write_push_pop('C_POP', 'temp', 0)

        # pop temp 1
        write_push_pop('C_POP', 'temp', 1)

        # lt
        # # store temp 0 in D
        output_file_data.write('@5\n')
        output_file_data.write('A=A+1\n')
        output_file_data.write('D=M\n')

        # # sub temp 0 from D
        output_file_data.write('A=A-1\n')
        output_file_data.write('D=D-M\n')

        # if D = 0 goto less_than
        output_file_data.write('@LESS_THAN_{}\n'.format(less_than_counter))
        output_file_data.write('D;JLT\n')

        # if D != 0 goto greater_or_equal
        output_file_data.write('@NOT_LESS_THAN_{}\n'.format(not_less_than_counter))
        output_file_data.write('D;JGE\n')

        # greater function
        output_file_data.write('(LESS_THAN_{})\n'.format(less_than_counter))
        less_than_counter += 1
        output_file_data.write('D=-1\n')
        output_file_data.write('@PUSH_{}\n'.format(push_counter))
        output_file_data.write('0;JMP\n')

        # not_greater function
        output_file_data.write('(NOT_LESS_THAN_{})\n'.format(not_less_than_counter))
        not_less_than_counter += 1
        output_file_data.write('D=0\n')
        output_file_data.write('@PUSH_{}\n'.format(push_counter))
        output_file_data.write('0;JMP\n')

        # push temp 0

        output_file_data.write('(PUSH_{})\n'.format(push_counter))

        # store D in temp 0
        output_file_data.write('@5\n')
        output_file_data.write('M=D\n')

        push_counter += 1
        write_push_pop('C_PUSH', 'temp', 0)
    elif command == 'and':

        # pop temp 0
        write_push_pop('C_POP', 'temp', 0)

        # pop temp 1
        write_push_pop('C_POP', 'temp', 1)

        # bit-wise and
        # # store temp 0 in D
        output_file_data.write('@5\n')
        output_file_data.write('D=M\n')

        # # temp 0 and temp 1
        output_file_data.write('A=A+1\n')
        output_file_data.write('M=D&M\n')

        # push temp 1
        # # store result of above addition in D
        output_file_data.write('D=M\n')

        # push temp 0

        # store D in temp 0
        output_file_data.write('@5\n')
        output_file_data.write('M=D\n')

        write_push_pop('C_PUSH', 'temp', 0)
    elif command == 'or':

        # pop temp 0
        write_push_pop('C_POP', 'temp', 0)

        # pop temp 1
        write_push_pop('C_POP', 'temp', 1)

        # bit-wise or
        # # store temp 0 in D
        output_file_data.write('@5\n')
        output_file_data.write('D=M\n')

        # # temp 0 and temp 1
        output_file_data.write('A=A+1\n')
        output_file_data.write('D=D|M\n')

        # push temp 0

        # store D in temp 0
        output_file_data.write('@5\n')
        output_file_data.write('M=D\n')

        write_push_pop('C_PUSH', 'temp', 0)
    elif command == 'not':
        # pop temp 0
        # # store top of stack in D
        output_file_data.write('@SP\n')
        output_file_data.write('M=M-1\n')
        output_file_data.write('A=M\n')
        output_file_data.write('D=M\n')
        # neg
        output_file_data.write('D=!D\n')
        # push temp 0

        # store D in temp 0
        output_file_data.write('@5\n')
        output_file_data.write('M=D\n')

        write_push_pop('C_PUSH', 'temp', 0)
    else:
        output_file_data.write('Error: cannot write command\n')


def write_push_pop(command, segment, index):

    # writes the assembly code that is the translation of the given command
    global output_file_data
    if command == 'C_PUSH':

        if segment == 'constant':
            # store index in D
            output_file_data.write('@{}\n'.format(index))
            output_file_data.write('D=A\n')

            # store D in *SP
            output_file_data.write('@SP\n')
            output_file_data.write('A=M\n')
            output_file_data.write('M=D\n')

            # increment SP
            output_file_data.write('@SP\n')
            output_file_data.write('M=M+1\n')
        elif segment == 'temp':
            output_file_data.write('@5\n')
            output_file_data.write('D=A\n')
            output_file_data.write('@{}\n'.format(index))
            output_file_data.write('A=D+A\n')
            output_file_data.write('D=M\n')

            # # store D in top of stack
            output_file_data.write('@SP\n')
            output_file_data.write('A=M\n')
            output_file_data.write('M=D\n')

            # # increment stack pointer
            output_file_data.write('@SP\n')
            output_file_data.write('M=M+1\n')
        elif segment == 'static':
            output_file_data.write('@{}{}\n'.format(input_file_name, index))
            output_file_data.write('D=M\n')

            # # store D in top of stack
            output_file_data.write('@SP\n')
            output_file_data.write('A=M\n')
            output_file_data.write('M=D\n')

            # # increment stack pointer
            output_file_data.write('@SP\n')
            output_file_data.write('M=M+1\n')
        elif segment == 'pointer':
            if index == 0:
                output_file_data.write('@THIS\n')
                output_file_data.write('D=M\n')
            elif index == 1:
                output_file_data.write('@THAT\n')
                output_file_data.write('D=M\n')

            output_file_data.write('@SP\n')
            output_file_data.write('A=M\n')
            output_file_data.write('M=D\n')

            output_file_data.write('@SP\n')
            output_file_data.write('M=M+1\n')
        else:
            if segment == 'local':
                # push local i
                output_file_data.write('@LCL\n')
            elif segment == 'argument':
                # push argument i
                output_file_data.write('@ARG\n')
            elif segment == 'this':
                output_file_data.write('@THIS\n')
            elif segment == 'that':
                output_file_data.write('@THAT\n')

            output_file_data.write('D=M\n')
            output_file_data.write('@{}\n'.format(index))
            output_file_data.write('A=D+A\n')
            output_file_data.write('D=M\n')

            # # store D in top of stack
            output_file_data.write('@SP\n')
            output_file_data.write('A=M\n')
            output_file_data.write('M=D\n')

            # # increment stack pointer
            output_file_data.write('@SP\n')
            output_file_data.write('M=M+1\n')
    elif command == 'C_POP':
        if segment == 'static':
            output_file_data.write('@SP\n')
            output_file_data.write('M=M-1\n')
            output_file_data.write('A=M\n')
            output_file_data.write('D=M\n')

            output_file_data.write('@{}{}\n'.format(input_file_name, index))
            output_file_data.write('M=D\n')
        elif segment == 'pointer':
            output_file_data.write('@SP\n')
            output_file_data.write('M=M-1\n')

            output_file_data.write('A=M\n')
            output_file_data.write('D=M\n')

            if index == 0:
                output_file_data.write('@THIS\n')
                output_file_data.write('M=D\n')
            elif index == 1:
                output_file_data.write('@THAT\n')
                output_file_data.write('M=D\n')
        else:
            if segment == 'local':
                output_file_data.write('@LCL\n')
                output_file_data.write('D=M\n')
            elif segment == 'argument':
                output_file_data.write('@ARG\n')
                output_file_data.write('D=M\n')
            elif segment == 'this':
                output_file_data.write('@THIS\n')
                output_file_data.write('D=M\n')
            elif segment == 'that':
                output_file_data.write('@THAT\n')
                output_file_data.write('D=M\n')
            elif segment == 'temp':
                output_file_data.write('@5\n')
                output_file_data.write('D=A\n')

            output_file_data.write('@{}\n'.format(index))
            output_file_data.write('D=D+A\n')

            output_file_data.write('@13\n')
            output_file_data.write('M=D\n')

            output_file_data.write('@SP\n')
            output_file_data.write('M=M-1\n')
            output_file_data.write('A=M\n')
            output_file_data.write('D=M\n')

            output_file_data.write('@13\n')
            output_file_data.write('A=M\n')
            output_file_data.write('M=D\n')


def close_file():
    global output_file_data

    output_file_data.write('(END)\n')
    output_file_data.write('@END\n')
    output_file_data.write('0;JMP\n')

    output_file_data.close()
