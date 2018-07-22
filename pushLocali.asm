@LCL   // store local 17 in D
D=M
@17
A=D+A
D=M
@SP    // store D in top of stack
A=M
M=D
@SP    // *SP++
M=M+1
@LCL   // store local 0 in D
D=M
@0
A=D+A
D=M
@SP    // store D in top of stack
A=M
M=D
@SP    // *SP++
M=M+1
@LCL   // store local 3 in D
D=M
@3
A=D+A
D=M
@SP    // store D in top of stack
A=M
M=D
@SP    // *SP++
M=M+1
(END)
@END
0;JMP
