@this    // store base address of this in D
D=A
@SP      // push D to the stack
A=M
M=D
@SP      // SP++
M=M+1
@that    // store base address of that in D
D=A
@SP      // push D to the stack
A=M
M=D
@SP      // SP++
M=M+1
@SP    // SP--
M=M-1
A=M    // store top of stack in D
D=M
@that  // store D in that
M=D
@SP    // SP--
M=M-1
A=M    // store top of stack in D
D=M
@this  // store D in this
M=D
(END)
@END
0;JMP
