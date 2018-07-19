// push  17
@17    // D = constant 17
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
// sub
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
M=M-D
D=M
// push local 1
@SP    // store D in top of stack
A=M
M=D
@SP    // *SP++
M=M+1
(END)
@END
0;JMP
