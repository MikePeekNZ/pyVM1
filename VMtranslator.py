# main module for VM translator stage 1: stack arithmetic commands

import sys
import os
import parser_module1
import code_writer_module1


def main():

    # check whether individual file or folder is passed to VMTranslator
    if sys.argv[1][len(sys.argv[1]) - 3] == '.' \
            and sys.argv[1][len(sys.argv[1]) - 2] == 'v' \
            and sys.argv[1][len(sys.argv[1]) - 1] == 'm':

        # open input file
        parser_module1.constructor(sys.argv[1])

        # open output file
        code_writer_module1.set_file_name(sys.argv[1])
    else:
        # extract list of files to copy
        file_list = os.listdir(sys.argv[1])

        # pass files to constructor
        for i in range(0, len(file_list)):
            parser_module1.constructor(file_list[i])

        # set output file
        code_writer_module1.set_file_name(sys.argv[1])

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

        # process arithmetic command
        if main_command_type == 'C_ARITHMETIC':
            code_writer_module1.write_arithmetic(argument_1)

    # close file
    code_writer_module1.close_file()


if __name__ == '__main__':
    main()
