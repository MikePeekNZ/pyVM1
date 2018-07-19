// push  8
@8    // D = constant 8
D=A
@SP    // *SP = D
A=M
M=D
@SP    // SP++
M=M+1
// push  9
@9    // D = constant 9
D=A
@SP    // *SP = D
A=M
M=D
@SP    // SP++
M=M+1
// gt
@SP    // store top of stack in D
M=M-1  // move pointer to top value on stack
A=M
D=M
@LCL    // store D in local 0
A=M
M=D
@SP    // store top of stack in D
M=M-1  // move pointer to top value on stack
A=M
D=M
@LCL   // store D in local 1
A=M
A=A+1
M=D
@LCL    // store local 0 in D
A=M
A=A+1
D=M
A=A-1
D=D-M
@GREATER
D;JGT
@NOT_GREATER
D;JLE
(GREATER)
D=-1
@PUSH
0;JMP
(NOT_GREATER)
D=0
@PUSH
0;JMP
// push local 0
(PUSH)
@SP    // store D in top of stack
A=M
M=D
@SP    // *SP++
M=M+1
(END)
@END
0;JMP
