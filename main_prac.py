# main module for VM translator stage 1: stack arithmetic commands

import sys
import os
from src import parser_module1
from src import code_writer_module1


def main():

    # check if reading folder or single file
    argument_vector_1 = sys.argv[1]
    len_argv1 = len(argument_vector_1)
    files_to_copy = []

    if argument_vector_1[len_argv1 - 3] == '.' \
            and argument_vector_1[len_argv1 - 2] == 'v' \
            and argument_vector_1[len_argv1 - 1] == 'm':

        parser_module1.constructor(sys.argv[1])
    else:
        folder_path = os.listdir('C:/Program_Files/mingw-w64/pyVM1/testFiles')
        for i in folder_path:
            files_to_copy.append(i)

        for i in range(0, len(files_to_copy)):

            # copy contents of infile
            parser_module1.constructor(files_to_copy[i])

    # open outfile
    if sys.argv[1][len(sys.argv[1]) - 3] == '.':
        code_writer_module1.set_file_name(sys.argv[1])
    else:
        file_name = sys.argv[1]
        file_name = file_name + '.vm'
        code_writer_module1.set_file_name(file_name)

    # loop through contents of input file data
    while parser_module1.has_more_commands():

        # load next command
        parser_module1.advance()

        # get command type of current command
        main_command_type = parser_module1.command_type()

        # get argument 1
        argument_1 = parser_module1.arg1()

        # get argument 2
        if main_command_type == 'C_PUSH' or main_command_type == 'C_POP':
            argument_2 = parser_module1.arg2()
            code_writer_module1.write_push_pop(main_command_type, argument_1,
                                               argument_2)

        if main_command_type == 'C_ARITHMETIC':
            code_writer_module1.write_arithmetic(argument_1)

    code_writer_module1.close_file()


if __name__ == '__main__':
    main()
