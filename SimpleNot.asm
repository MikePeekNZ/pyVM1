// push  17
@17    // D = constant 17
D=A
@SP    // *SP = D
A=M
M=D
@SP    // SP++
M=M+1
// not
@SP    // store top of stack in D
M=M-1  // move pointer to top value on stack
A=M
D=M
D=!D   // D gets not D
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
