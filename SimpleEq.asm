// push  7
@7    // D = constant 7
D=A
@SP    // *SP = D
A=M
M=D
@SP    // SP++
M=M+1
// push  8
@8    // D = constant 8
D=A
@SP    // *SP = D
A=M
M=D
@SP    // SP++
M=M+1
// eq
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
D=M
A=A+1
D=D-M
@EQUAL
D;JEQ
@UNEQUAL
D;JNE
(EQUAL)
D=-1
@PUSH
0;JMP
(UNEQUAL)
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
