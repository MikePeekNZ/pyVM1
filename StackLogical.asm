// push  17
@17    // D = constant 17
D=A
@SP    // *SP = D
A=M
M=D
@SP    // SP++
M=M+1
// push  17
@17    // D = constant 17
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
D=D-M
@EQUAL_0
D;JEQ
@NOT_EQUAL_0
D;JNE
(EQUAL_0)
D=-1
@PUSH_0
0;JMP
(NOT_EQUAL_0)
D=0
@PUSH_0
0;JMP
// push local 0
(PUSH_0)
@SP    // store D in top of stack
A=M
M=D
@SP    // *SP++
M=M+1
// push  17
@17    // D = constant 17
D=A
@SP    // *SP = D
A=M
M=D
@SP    // SP++
M=M+1
// push  16
@16    // D = constant 16
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
D=D-M
@EQUAL_1
D;JEQ
@NOT_EQUAL_1
D;JNE
(EQUAL_1)
D=-1
@PUSH_1
0;JMP
(NOT_EQUAL_1)
D=0
@PUSH_1
0;JMP
// push local 0
(PUSH_1)
@SP    // store D in top of stack
A=M
M=D
@SP    // *SP++
M=M+1
// push  16
@16    // D = constant 16
D=A
@SP    // *SP = D
A=M
M=D
@SP    // SP++
M=M+1
// push  17
@17    // D = constant 17
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
D=D-M
@EQUAL_2
D;JEQ
@NOT_EQUAL_2
D;JNE
(EQUAL_2)
D=-1
@PUSH_2
0;JMP
(NOT_EQUAL_2)
D=0
@PUSH_2
0;JMP
// push local 0
(PUSH_2)
@SP    // store D in top of stack
A=M
M=D
@SP    // *SP++
M=M+1
// push  892
@892    // D = constant 892
D=A
@SP    // *SP = D
A=M
M=D
@SP    // SP++
M=M+1
// push  891
@891    // D = constant 891
D=A
@SP    // *SP = D
A=M
M=D
@SP    // SP++
M=M+1
// lt
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
A=A+1
D=M
A=A-1
D=D-M
@LESS_THAN_0
D;JLT
@NOT_LESS_THAN_0
D;JGE
(LESS_THAN_0)
D=-1
@PUSH_3
0;JMP
(NOT_LESS_THAN_0)
D=0
@PUSH_3
0;JMP
// push local 0
(PUSH_3)
@SP    // store D in top of stack
A=M
M=D
@SP    // *SP++
M=M+1
// push  891
@891    // D = constant 891
D=A
@SP    // *SP = D
A=M
M=D
@SP    // SP++
M=M+1
// push  892
@892    // D = constant 892
D=A
@SP    // *SP = D
A=M
M=D
@SP    // SP++
M=M+1
// lt
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
A=A+1
D=M
A=A-1
D=D-M
@LESS_THAN_1
D;JLT
@NOT_LESS_THAN_1
D;JGE
(LESS_THAN_1)
D=-1
@PUSH_4
0;JMP
(NOT_LESS_THAN_1)
D=0
@PUSH_4
0;JMP
// push local 0
(PUSH_4)
@SP    // store D in top of stack
A=M
M=D
@SP    // *SP++
M=M+1
// push  891
@891    // D = constant 891
D=A
@SP    // *SP = D
A=M
M=D
@SP    // SP++
M=M+1
// push  891
@891    // D = constant 891
D=A
@SP    // *SP = D
A=M
M=D
@SP    // SP++
M=M+1
// lt
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
A=A+1
D=M
A=A-1
D=D-M
@LESS_THAN_2
D;JLT
@NOT_LESS_THAN_2
D;JGE
(LESS_THAN_2)
D=-1
@PUSH_5
0;JMP
(NOT_LESS_THAN_2)
D=0
@PUSH_5
0;JMP
// push local 0
(PUSH_5)
@SP    // store D in top of stack
A=M
M=D
@SP    // *SP++
M=M+1
// push  32767
@32767    // D = constant 32767
D=A
@SP    // *SP = D
A=M
M=D
@SP    // SP++
M=M+1
// push  32766
@32766    // D = constant 32766
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
A=A+1
D=M
A=A-1
D=D-M
@GREATER_0
D;JGT
@NOT_GREATER_0
D;JLE
(GREATER_0)
D=-1
@PUSH_6
0;JMP
(NOT_GREATER_0)
D=0
@PUSH_6
0;JMP
// push local 0
(PUSH_6)
@SP    // store D in top of stack
A=M
M=D
@SP    // *SP++
M=M+1
// push  32766
@32766    // D = constant 32766
D=A
@SP    // *SP = D
A=M
M=D
@SP    // SP++
M=M+1
// push  32767
@32767    // D = constant 32767
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
A=A+1
D=M
A=A-1
D=D-M
@GREATER_1
D;JGT
@NOT_GREATER_1
D;JLE
(GREATER_1)
D=-1
@PUSH_7
0;JMP
(NOT_GREATER_1)
D=0
@PUSH_7
0;JMP
// push local 0
(PUSH_7)
@SP    // store D in top of stack
A=M
M=D
@SP    // *SP++
M=M+1
// push  32766
@32766    // D = constant 32766
D=A
@SP    // *SP = D
A=M
M=D
@SP    // SP++
M=M+1
// push  32766
@32766    // D = constant 32766
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
A=A+1
D=M
A=A-1
D=D-M
@GREATER_2
D;JGT
@NOT_GREATER_2
D;JLE
(GREATER_2)
D=-1
@PUSH_8
0;JMP
(NOT_GREATER_2)
D=0
@PUSH_8
0;JMP
// push local 0
(PUSH_8)
@SP    // store D in top of stack
A=M
M=D
@SP    // *SP++
M=M+1
(END)
@END
0;JMP
