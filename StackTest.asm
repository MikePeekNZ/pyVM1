@17
D=A
@SP
A=M
M=D
@SP
M=M+1
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
@5
D=A
@0
D=D+A
@13
M=D
@SP
M=M-1
A=M
D=M
@13
A=M
M=D
@5
D=A
@1
D=D+A
@13
M=D
@SP
M=M-1
A=M
D=M
@13
A=M
M=D
@5
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
(PUSH_0)
@5
M=D
@5
D=A
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
@5
D=A
@0
D=D+A
@13
M=D
@SP
M=M-1
A=M
D=M
@13
A=M
M=D
@5
D=A
@1
D=D+A
@13
M=D
@SP
M=M-1
A=M
D=M
@13
A=M
M=D
@5
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
(PUSH_1)
@5
M=D
@5
D=A
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
@5
D=A
@0
D=D+A
@13
M=D
@SP
M=M-1
A=M
D=M
@13
A=M
M=D
@5
D=A
@1
D=D+A
@13
M=D
@SP
M=M-1
A=M
D=M
@13
A=M
M=D
@5
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
(PUSH_2)
@5
M=D
@5
D=A
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
@5
D=A
@0
D=D+A
@13
M=D
@SP
M=M-1
A=M
D=M
@13
A=M
M=D
@5
D=A
@1
D=D+A
@13
M=D
@SP
M=M-1
A=M
D=M
@13
A=M
M=D
@5
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
(PUSH_3)
@5
M=D
@5
D=A
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
@5
D=A
@0
D=D+A
@13
M=D
@SP
M=M-1
A=M
D=M
@13
A=M
M=D
@5
D=A
@1
D=D+A
@13
M=D
@SP
M=M-1
A=M
D=M
@13
A=M
M=D
@5
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
(PUSH_4)
@5
M=D
@5
D=A
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
@5
D=A
@0
D=D+A
@13
M=D
@SP
M=M-1
A=M
D=M
@13
A=M
M=D
@5
D=A
@1
D=D+A
@13
M=D
@SP
M=M-1
A=M
D=M
@13
A=M
M=D
@5
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
(PUSH_5)
@5
M=D
@5
D=A
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@5
D=A
@0
D=D+A
@13
M=D
@SP
M=M-1
A=M
D=M
@13
A=M
M=D
@5
D=A
@1
D=D+A
@13
M=D
@SP
M=M-1
A=M
D=M
@13
A=M
M=D
@5
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
(PUSH_6)
@5
M=D
@5
D=A
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
@5
D=A
@0
D=D+A
@13
M=D
@SP
M=M-1
A=M
D=M
@13
A=M
M=D
@5
D=A
@1
D=D+A
@13
M=D
@SP
M=M-1
A=M
D=M
@13
A=M
M=D
@5
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
(PUSH_7)
@5
M=D
@5
D=A
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@5
D=A
@0
D=D+A
@13
M=D
@SP
M=M-1
A=M
D=M
@13
A=M
M=D
@5
D=A
@1
D=D+A
@13
M=D
@SP
M=M-1
A=M
D=M
@13
A=M
M=D
@5
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
(PUSH_8)
@5
M=D
@5
D=A
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
@57
D=A
@SP
A=M
M=D
@SP
M=M+1
@31
D=A
@SP
A=M
M=D
@SP
M=M+1
@53
D=A
@SP
A=M
M=D
@SP
M=M+1
@5
D=A
@0
D=D+A
@13
M=D
@SP
M=M-1
A=M
D=M
@13
A=M
M=D
@5
D=A
@1
D=D+A
@13
M=D
@SP
M=M-1
A=M
D=M
@13
A=M
M=D
@5
D=M
A=A+1
D=D+M
@5
M=D
@5
D=A
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
@112
D=A
@SP
A=M
M=D
@SP
M=M+1
@5
D=A
@0
D=D+A
@13
M=D
@SP
M=M-1
A=M
D=M
@13
A=M
M=D
@5
D=A
@1
D=D+A
@13
M=D
@SP
M=M-1
A=M
D=M
@13
A=M
M=D
@5
D=M
A=A+1
D=M-D
@5
M=D
@5
D=A
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
A=M
M=-M
D=M
@5
M=D
@5
D=A
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
@5
D=A
@0
D=D+A
@13
M=D
@SP
M=M-1
A=M
D=M
@13
A=M
M=D
@5
D=A
@1
D=D+A
@13
M=D
@SP
M=M-1
A=M
D=M
@13
A=M
M=D
@5
D=M
A=A+1
M=D&M
D=M
@5
M=D
@5
D=A
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
@82
D=A
@SP
A=M
M=D
@SP
M=M+1
@5
D=A
@0
D=D+A
@13
M=D
@SP
M=M-1
A=M
D=M
@13
A=M
M=D
@5
D=A
@1
D=D+A
@13
M=D
@SP
M=M-1
A=M
D=M
@13
A=M
M=D
@5
D=M
A=A+1
D=D|M
@5
M=D
@5
D=A
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
A=M
D=M
D=!D
@5
M=D
@5
D=A
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
(END)
@END
0;JMP
