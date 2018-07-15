# main module for VM translator stage 1: stack arithmetic commands

import sys
from src import parser_module1


def main():

    # copy contents of .vm into programme
    parser_module1.constructor(sys.argv[1])

    # create empty string to store name of output_file
    output_file = ''

    # set name of output file to that of input file
    for char in sys.argv[1]:
        output_file = output_file + char

    # remove file type ending
    output_file = output_file[0:len(output_file) - 2]

    # add asm as the file type
    output_file = output_file + 'asm'

    # open the output file for writing
    with open(output_file, 'w') as output_file:
        output_file.write('words words words' + '\n')


if __name__ == '__main__':
    main()
