@LCL   // store local 0 in D
D=M    // add index to LCL value
@0
D=D+A
@5  // store local i in temp
M=D
@SP    // store top of stack in D
M=M-1
A=M
D=M
@5     // store top of stack in local i
A=M
M=D
@LCL   // store local 1 in D
D=M    // add index to LCL value
@1
D=D+A
@5  // store local i in temp
M=D
@SP    // store top of stack in D
M=M-1
A=M
D=M
@5     // store top of stack in local i
A=M
M=D
@LCL   // store local 2 in D
D=M    // add index to LCL value
@2
D=D+A
@5  // store local i in temp
M=D
@SP    // store top of stack in D
M=M-1
A=M
D=M
@5     // store top of stack in local i
A=M
M=D
(END)
@END
0;JMP
