# main module for VM translator stage 1: stack arithmetic commands

import sys
from src import parser_module1
from src import code_writer_module1


def main():

    # copy contents of infile
    parser_module1.constructor(sys.argv[1])

    # open outfile
    code_writer_module1.set_file_name(sys.argv[1])

    # loop through contents of input file data
    while parser_module1.has_more_commands():

        # prepare to store command_type
        # main_command_type = ''

        # load next command
        parser_module1.advance()

        # get command type of current command
        main_command_type = parser_module1.command_type()

        # get argument 1
        argument_1 = parser_module1.arg1()

        # get argument 2
        if main_command_type == 'C_PUSH':
            argument_2 = parser_module1.arg2()
            code_writer_module1.write_push_pop(main_command_type, argument_1,
                                               argument_2)

        if main_command_type == 'C_ARITHMETIC':
            code_writer_module1.write_arithmetic(argument_1)

    code_writer_module1.close_file()

    # for i in range(0, len(parser_module1.read_data)):
    # print(parser_module1.read_data[i])

    # print(parser_module1.read_data)

    # code_writer_module1.close_file()


if __name__ == '__main__':
    main()
