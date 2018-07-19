// push  7
@7    // D = constant 7
D=A
@SP    // *SP = D
A=M
M=D
@SP    // SP++
M=M+1
// push  12
@12    // D = constant 12
D=A
@SP    // *SP = D
A=M
M=D
@SP    // SP++
M=M+1
// or
@SP    // store top of stack in D
M=M-1  // move pointer to top value on stack
A=M
D=M
@16    // store D in local 0
M=D
@SP    // store top of stack in D
M=M-1  // move pointer to top value on stack
A=M
D=M
@16   // store D in local 1
A=A+1
M=D
@16    // store local 0 in D
D=M
A=A+1
M=D|M
D=M
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
