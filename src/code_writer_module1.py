# codewriter module for VM translator stage 1: stack arithmetic commands
output_file_data = {}
output_file_name = ''


def set_file_name(filename):
    global output_file_data
    global output_file_name

    # copy name of input file
    for char in filename:
        output_file_name = output_file_name + char

    # remove file type ending
    output_file_name = output_file_name[0:len(output_file_name) - 2]

    # add asm as file type
    output_file_name = output_file_name + 'asm'

    # Opens the output file/stream and gets ready to write into it
    output_file_data = open(output_file_name, 'w', encoding='utf-8')


def write_arithmetic(command):
    global output_file_data

    # Writes the assembly code that is the translation of the given
    # arithmetic command
    if command == 'add':
        output_file_data.write('// add\n')

        # pop local 0
        # # store top of stack in D
        output_file_data.write('@SP    // store top of stack in D\n')
        output_file_data.write('M=M-1  // move pointer to top value on stack\n')
        output_file_data.write('A=M\n')
        output_file_data.write('D=M\n')

        # # store D in local 0
        output_file_data.write('@LCL    // store D in local 0\n')
        output_file_data.write('A=M\n')
        output_file_data.write('M=D\n')

        # # decrement stack pointer
        output_file_data.write('@SP    // *SP--\n')
        output_file_data.write('M=M-1\n')

        # pop local 1
        # # store top of stack in D
        output_file_data.write('@SP    // store top of stack in D\n')
        output_file_data.write('A=M\n')
        output_file_data.write('D=M\n')

        # # store D in local 1
        output_file_data.write('@LCL   // store D in local 1\n')
        output_file_data.write('A=M\n')
        output_file_data.write('A=A+1\n')
        output_file_data.write('M=D\n')

        # add
        # # store local 0 in D
        output_file_data.write('@LCL    // store local 0 in D\n')
        output_file_data.write('A=M\n')
        output_file_data.write('D=M\n')

        # # Add D to local 1
        output_file_data.write('A=A+1\n')
        output_file_data.write('M=D+M\n')

        # # store result of previous calculation in D
        output_file_data.write('D=M\n')

        # push local 1
        output_file_data.write('// push local 1\n')
        write_push_pop('C_PUSH', 'local', 1)
    elif command == 'sub':
        output_file_data.write('// sub\n')

        # pop local 0
        # # store top of stack in D
        output_file_data.write('@SP    // store top of stack in D\n')
        output_file_data.write('M=M-1  // move pointer to top value on stack\n')
        output_file_data.write('A=M\n')
        output_file_data.write('D=M\n')

        # # store D in local 0
        output_file_data.write('@LCL    // store D in local 0\n')
        output_file_data.write('A=M\n')
        output_file_data.write('M=D\n')

        # # decrement stack pointer
        output_file_data.write('@SP    // *SP--\n')
        output_file_data.write('M=M-1\n')

        # pop local 1
        # # store top of stack in D
        output_file_data.write('@SP    // store top of stack in D\n')
        output_file_data.write('A=M\n')
        output_file_data.write('D=M\n')

        # # store D in local 1
        output_file_data.write('@LCL   // store D in local 1\n')
        output_file_data.write('A=M\n')
        output_file_data.write('A=A+1\n')
        output_file_data.write('M=D\n')

        # sub
        # # store local 0 in D
        output_file_data.write('@LCL    // store local 0 in D\n')
        output_file_data.write('A=M\n')
        output_file_data.write('D=M\n')

        # # sub D from local 1
        output_file_data.write('A=A+1\n')
        output_file_data.write('M=M-D\n')

        # # store result of previous calculation in D
        output_file_data.write('D=M\n')

        # push local 1
        output_file_data.write('// push local 1\n')
        write_push_pop('C_PUSH', 'local', 1)
    elif command == 'neg':
        output_file_data.write('// neg\n')
        # pop local 0
        # # store top of stack in D
        output_file_data.write('@SP    // store top of stack in D\n')
        output_file_data.write('M=M-1  // move pointer to top value on stack\n')
        output_file_data.write('A=M\n')
        # neg
        output_file_data.write('M=-M\n')
        # neg

        # # store result of previous calculation in D
        output_file_data.write('D=M\n')

        # push local 0
        output_file_data.write('// push local 0\n')
        write_push_pop('C_PUSH', 'local', 0)
    elif command == 'eq':
        output_file_data.write('// eq\n')
        # pop local 0
        # # store top of stack in D
        output_file_data.write('@SP    // store top of stack in D\n')
        output_file_data.write('M=M-1  // move pointer to top value on stack\n')
        output_file_data.write('A=M\n')
        output_file_data.write('D=M\n')

        # # store D in local 0
        output_file_data.write('@LCL    // store D in local 0\n')
        output_file_data.write('A=M\n')
        output_file_data.write('M=D\n')

        # # decrement stack pointer
        output_file_data.write('@SP    // *SP--\n')
        output_file_data.write('M=M-1\n')

        # pop local 1
        # # store top of stack in D
        output_file_data.write('@SP    // store top of stack in D\n')
        output_file_data.write('A=M\n')
        output_file_data.write('D=M\n')

        # # store D in local 1
        output_file_data.write('@LCL   // store D in local 1\n')
        output_file_data.write('A=M\n')
        output_file_data.write('A=A+1\n')
        output_file_data.write('M=D\n')

        # eq
        # # store local 0 in D
        output_file_data.write('@LCL    // store local 0 in D\n')
        output_file_data.write('A=M\n')
        output_file_data.write('D=M\n')

        # # sub local 1 from D
        output_file_data.write('A=A+1\n')
        output_file_data.write('D=D-M\n')

        # if D = 0 goto equal
        output_file_data.write('@EQUAL\n')
        output_file_data.write('D;JEQ\n')

        # if D != 0 goto unequal
        output_file_data.write('@UNEQUAL\n')
        output_file_data.write('D;JNE\n')

        # equal function
        output_file_data.write('(EQUAL)\n')
        output_file_data.write('D=-1\n')
        output_file_data.write('@PUSH\n')
        output_file_data.write('0;JMP\n')

        # unequal function
        output_file_data.write('(UNEQUAL)\n')
        output_file_data.write('D=0\n')
        output_file_data.write('@PUSH\n')
        output_file_data.write('0;JMP\n')

        # push local 0
        output_file_data.write('// push local 0\n')

        output_file_data.write('(PUSH)\n')
        write_push_pop('C_PUSH', 'local', 0)
    elif command == 'gt':
        output_file_data.write('// gt\n')
        # pop local 0
        # # store top of stack in D
        output_file_data.write('@SP    // store top of stack in D\n')
        output_file_data.write('M=M-1  // move pointer to top value on stack\n')
        output_file_data.write('A=M\n')
        output_file_data.write('D=M\n')

        # # store D in local 0
        output_file_data.write('@LCL    // store D in local 0\n')
        output_file_data.write('A=M\n')
        output_file_data.write('M=D\n')

        # # decrement stack pointer
        output_file_data.write('@SP    // *SP--\n')
        output_file_data.write('M=M-1\n')

        # pop local 1
        # # store top of stack in D
        output_file_data.write('@SP    // store top of stack in D\n')
        output_file_data.write('A=M\n')
        output_file_data.write('D=M\n')

        # # store D in local 1
        output_file_data.write('@LCL   // store D in local 1\n')
        output_file_data.write('A=M\n')
        output_file_data.write('A=A+1\n')
        output_file_data.write('M=D\n')

        # gt
        # # store local 1 in D
        output_file_data.write('@LCL    // store local 0 in D\n')
        output_file_data.write('A=M\n')
        output_file_data.write('A=A+1\n')
        output_file_data.write('D=M\n')

        # # sub local 0 from D
        output_file_data.write('A=A-1\n')
        output_file_data.write('D=D-M\n')

        # if D = 0 goto greater
        output_file_data.write('@GREATER\n')
        output_file_data.write('D;JGT\n')

        # if D != 0 goto not_greater
        output_file_data.write('@NOT_GREATER\n')
        output_file_data.write('D;JLE\n')

        # greater function
        output_file_data.write('(GREATER)\n')
        output_file_data.write('D=-1\n')
        output_file_data.write('@PUSH\n')
        output_file_data.write('0;JMP\n')

        # not_greater function
        output_file_data.write('(NOT_GREATER)\n')
        output_file_data.write('D=0\n')
        output_file_data.write('@PUSH\n')
        output_file_data.write('0;JMP\n')

        # push local 0
        output_file_data.write('// push local 0\n')

        output_file_data.write('(PUSH)\n')
        write_push_pop('C_PUSH', 'local', 0)
    elif command == 'lt':
        output_file_data.write('// lt\n')
        # pop local 0
        # # store top of stack in D
        output_file_data.write('@SP    // store top of stack in D\n')
        output_file_data.write('M=M-1  // move pointer to top value on stack\n')
        output_file_data.write('A=M\n')
        output_file_data.write('D=M\n')

        # # store D in local 0
        output_file_data.write('@LCL    // store D in local 0\n')
        output_file_data.write('A=M\n')
        output_file_data.write('M=D\n')

        # # decrement stack pointer
        output_file_data.write('@SP    // *SP--\n')
        output_file_data.write('M=M-1\n')

        # pop local 1
        # # store top of stack in D
        output_file_data.write('@SP    // store top of stack in D\n')
        output_file_data.write('A=M\n')
        output_file_data.write('D=M\n')

        # # store D in local 1
        output_file_data.write('@LCL   // store D in local 1\n')
        output_file_data.write('A=M\n')
        output_file_data.write('A=A+1\n')
        output_file_data.write('M=D\n')

        # lt
        # # store local 0 in D
        output_file_data.write('@LCL    // store local 0 in D\n')
        output_file_data.write('A=M\n')
        output_file_data.write('A=A+1\n')
        output_file_data.write('D=M\n')

        # # sub local 0 from D
        output_file_data.write('A=A-1\n')
        output_file_data.write('D=D-M\n')

        # if D = 0 goto less_than
        output_file_data.write('@LESS_THAN\n')
        output_file_data.write('D;JLT\n')

        # if D != 0 goto greater_or_equal
        output_file_data.write('@GREATER_OR_EQUAL\n')
        output_file_data.write('D;JGE\n')

        # greater function
        output_file_data.write('(LESS_THAN)\n')
        output_file_data.write('D=-1\n')
        output_file_data.write('@PUSH\n')
        output_file_data.write('0;JMP\n')

        # not_greater function
        output_file_data.write('(GREATER_OR_EQUAL)\n')
        output_file_data.write('D=0\n')
        output_file_data.write('@PUSH\n')
        output_file_data.write('0;JMP\n')

        # push local 0
        output_file_data.write('// push local 0\n')

        output_file_data.write('(PUSH)\n')
        write_push_pop('C_PUSH', 'local', 0)
    elif command == 'and':
        output_file_data.write('// and\n')

        # pop local 0
        # # store top of stack in D
        output_file_data.write('@SP    // store top of stack in D\n')
        output_file_data.write('M=M-1  // move pointer to top value on stack\n')
        output_file_data.write('A=M\n')
        output_file_data.write('D=M\n')

        # # store D in local 0
        output_file_data.write('@LCL    // store D in local 0\n')
        output_file_data.write('A=M\n')
        output_file_data.write('M=D\n')

        # # decrement stack pointer
        output_file_data.write('@SP    // *SP--\n')
        output_file_data.write('M=M-1\n')

        # pop local 1
        # # store top of stack in D
        output_file_data.write('@SP    // store top of stack in D\n')
        output_file_data.write('A=M\n')
        output_file_data.write('D=M\n')

        # # store D in local 1
        output_file_data.write('@LCL   // store D in local 1\n')
        output_file_data.write('A=M\n')
        output_file_data.write('A=A+1\n')
        output_file_data.write('M=D\n')

        # bit-wise and
        # # store local 0 in D
        output_file_data.write('@LCL    // store local 0 in D\n')
        output_file_data.write('A=M\n')
        output_file_data.write('D=M\n')

        # # local 0 and local 1
        output_file_data.write('A=A+1\n')
        output_file_data.write('M=D&M\n')

        # push local 1
        # # store result of above addition in D
        output_file_data.write('D=M\n')

        # push local 0
        output_file_data.write('// push local 0\n')

        output_file_data.write('(PUSH)\n')
        write_push_pop('C_PUSH', 'local', 0)
    elif command == 'or':
        output_file_data.write('// or\n')

        # pop local 0
        # # store top of stack in D
        output_file_data.write('@SP    // store top of stack in D\n')
        output_file_data.write('M=M-1  // move pointer to top value on stack\n')
        output_file_data.write('A=M\n')
        output_file_data.write('D=M\n')

        # # store D in local 0
        output_file_data.write('@LCL    // store D in local 0\n')
        output_file_data.write('A=M\n')
        output_file_data.write('M=D\n')

        # # decrement stack pointer
        output_file_data.write('@SP    // *SP--\n')
        output_file_data.write('M=M-1\n')

        # pop local 1
        # # store top of stack in D
        output_file_data.write('@SP    // store top of stack in D\n')
        output_file_data.write('A=M\n')
        output_file_data.write('D=M\n')

        # # store D in local 1
        output_file_data.write('@LCL   // store D in local 1\n')
        output_file_data.write('A=M\n')
        output_file_data.write('A=A+1\n')
        output_file_data.write('M=D\n')

        # bit-wise or
        # # store local 0 in D
        output_file_data.write('@LCL    // store local 0 in D\n')
        output_file_data.write('A=M\n')
        output_file_data.write('D=M\n')

        # # local 0 and local 1
        output_file_data.write('A=A+1\n')
        output_file_data.write('M=D|M\n')

        # push local 1
        # # store result of above addition in D
        output_file_data.write('D=M\n')

        # push local 0
        output_file_data.write('// push local 0\n')

        output_file_data.write('(PUSH)\n')
        write_push_pop('C_PUSH', 'local', 0)
    elif command == 'not':
        output_file_data.write('// not\n')
        # pop local 0
        # # store top of stack in D
        output_file_data.write('@SP    // store top of stack in D\n')
        output_file_data.write('M=M-1  // move pointer to top value on stack\n')
        output_file_data.write('A=M\n')
        output_file_data.write('D=M\n')
        # neg
        output_file_data.write('D=!D   // D gets not D\n')
        # push local 0
        output_file_data.write('// push local 0\n')

        output_file_data.write('(PUSH)\n')
        write_push_pop('C_PUSH', 'local', 0)
    else:
        output_file_data.write('Error: cannot write command\n')


def write_push_pop(command, segment, index):

    # writes the assembly code that is the translation of the given command
    global output_file_data
    if command == 'C_PUSH':
        if segment == 'constant':
            # print command and segment to silence error message
            output_file_data.write('// push ' + ' {}'.format(index) + '\n')

            # store index in D
            output_file_data.write('@{}    // D = {} {}'.format(index, segment, index) + '\n')
            output_file_data.write('D=A' + '\n')

            # store D in *SP
            output_file_data.write('@SP    // *SP = D\n')
            output_file_data.write('A=M\n')
            output_file_data.write('M=D\n')

            # increment SP
            output_file_data.write('@SP    // SP++\n')
            output_file_data.write('M=M+1\n')
        elif segment == 'local':
            # push local index
            # # store result of previous calculation in D
            # output_file_data.write('D=M\n')

            # # store D in top of stack
            output_file_data.write('@SP    // store D in top of stack\n')
            output_file_data.write('A=M\n')
            output_file_data.write('M=D\n')

            # # increment stack pointer
            output_file_data.write('@SP    // *SP++\n')
            output_file_data.write('M=M+1\n')


def close_file():
    global output_file_data

    output_file_data.write('(END)\n')
    output_file_data.write('@END\n')
    output_file_data.write('0;JMP\n')

    output_file_data.close()
