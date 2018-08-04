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
@LCL   // store local 1 in D
D=M
@1
A=D+A
D=M
@SP    // store D in top of stack
A=M
M=D
@SP    // *SP++
M=M+1
// push  18
@18    // D = constant 18
D=A
@SP    // *SP = D
A=M
M=D
@SP    // SP++
M=M+1
// push  19
@19    // D = constant 19
D=A
@SP    // *SP = D
A=M
M=D
@SP    // SP++
M=M+1
@ARG   // store argument 2 in D
D=M
@2
A=D+A
D=M
@SP    // store D in top of stack
A=M
M=D
@SP    // *SP++
M=M+1
@ARG   // store argument 3 in D
D=M
@3
A=D+A
D=M
@SP    // store D in top of stack
A=M
M=D
@SP    // *SP++
M=M+1
@THIS  // store this 4 in D
D=M
@4
A=D+A
D=M
@SP    // store D in top of stack
A=M
M=D
@SP    // *SP++
M=M+1
@THIS  // store this 5 in D
D=M
@5
A=D+A
D=M
@SP    // store D in top of stack
A=M
M=D
@SP    // *SP++
M=M+1
@THAT  // store that 6 in D
D=M
@6
A=D+A
D=M
@SP    // store D in top of stack
A=M
M=D
@SP    // *SP++
M=M+1
@THAT  // store that 7 in D
D=M
@7
A=D+A
D=M
@SP    // store D in top of stack
A=M
M=D
@SP    // *SP++
M=M+1
@5     // store temp 6 in D
D=A
@6
A=D+A
D=M
@SP    // store D in top of stack
A=M
M=D
@SP    // *SP++
M=M+1
@pushSegmenti.8
D=M
@SP    // store D in top of stack
A=M
M=D
@SP    // *SP++
M=M+1
(END)
@END
0;JMP
