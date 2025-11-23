.data
   str_nl:.asciz "\n"

.text

L0: j Lmain
   
#======================================================
#Nesting level: 1 #Scope offset:28
#Parameter n Type int Pass CV Offset 12  | TemporaryVariable T@0 Datatype int Offset 16 | TemporaryVariable T@1 Datatype int Offset 20 | TemporaryVariable T@2 Datatype int Offset 24
#======================================================

   #Quad: 1 : begin_block, παραγοντικό, _, _
L1: 
   
#======================================================
#Nesting level: 1 #Scope offset:28
#Parameter n Type int Pass CV Offset 12  | TemporaryVariable T@0 Datatype int Offset 16 | TemporaryVariable T@1 Datatype int Offset 20 | TemporaryVariable T@2 Datatype int Offset 24
#======================================================

   #Quad: 2 : out, n, _, _
L2: 
   sw ra, 0(sp)
   lw t1, -12(sp)
   mv  a0, t1
   li a7, 1
   ecall
   la a0, str_nl
   li a7, 4
   ecall
   
#======================================================
#Nesting level: 1 #Scope offset:28
#Parameter n Type int Pass CV Offset 12  | TemporaryVariable T@0 Datatype int Offset 16 | TemporaryVariable T@1 Datatype int Offset 20 | TemporaryVariable T@2 Datatype int Offset 24
#======================================================

   #Quad: 3 : =, n, 0, 5
L3: 
   lw t1, -12(sp)
   li t2, 0
   beq t1, t2, L5
   
#======================================================
#Nesting level: 1 #Scope offset:28
#Parameter n Type int Pass CV Offset 12  | TemporaryVariable T@0 Datatype int Offset 16 | TemporaryVariable T@1 Datatype int Offset 20 | TemporaryVariable T@2 Datatype int Offset 24
#======================================================

   #Quad: 4 : jump, _, _, 7
L4: 
   j L7
   
#======================================================
#Nesting level: 1 #Scope offset:28
#Parameter n Type int Pass CV Offset 12  | TemporaryVariable T@0 Datatype int Offset 16 | TemporaryVariable T@1 Datatype int Offset 20 | TemporaryVariable T@2 Datatype int Offset 24
#======================================================

   #Quad: 5 : retv, 1, _, _
L5: 
   li t1, 1
   lw t0, -8(sp)
   sw t1, 0(t0)
   
#======================================================
#Nesting level: 1 #Scope offset:28
#Parameter n Type int Pass CV Offset 12  | TemporaryVariable T@0 Datatype int Offset 16 | TemporaryVariable T@1 Datatype int Offset 20 | TemporaryVariable T@2 Datatype int Offset 24
#======================================================

   #Quad: 6 : jump, _, _, 13
L6: 
   j L13
   
#======================================================
#Nesting level: 1 #Scope offset:28
#Parameter n Type int Pass CV Offset 12  | TemporaryVariable T@0 Datatype int Offset 16 | TemporaryVariable T@1 Datatype int Offset 20 | TemporaryVariable T@2 Datatype int Offset 24
#======================================================

   #Quad: 7 : -, n, 1, T@0
L7: 
   lw t1, -12(sp)
   li t2, 1
   sub t1, t1, t2
   sw t1, -16(sp)
   
#======================================================
#Nesting level: 1 #Scope offset:28
#Parameter n Type int Pass CV Offset 12  | TemporaryVariable T@0 Datatype int Offset 16 | TemporaryVariable T@1 Datatype int Offset 20 | TemporaryVariable T@2 Datatype int Offset 24
#======================================================

   #Quad: 8 : par, T@0, CV, _
L8: 
   addi fp, sp, 28
   lw t0, -16(sp)
   sw t0, -12(fp)
   
#======================================================
#Nesting level: 1 #Scope offset:28
#Parameter n Type int Pass CV Offset 12  | TemporaryVariable T@0 Datatype int Offset 16 | TemporaryVariable T@1 Datatype int Offset 20 | TemporaryVariable T@2 Datatype int Offset 24
#======================================================

   #Quad: 9 : par, T@1, RET, _
L9: 
   addi t0, sp, -20
   sw t0, -8(fp)
   
#======================================================
#Nesting level: 1 #Scope offset:28
#Parameter n Type int Pass CV Offset 12  | TemporaryVariable T@0 Datatype int Offset 16 | TemporaryVariable T@1 Datatype int Offset 20 | TemporaryVariable T@2 Datatype int Offset 24
#======================================================

   #Quad: 10 : call, παραγοντικό, _, _
L10: 
   lw t0, -4(sp)
   sw t0, -4(fp)
   addi sp, sp, 28
   jal L2
   addi sp, sp, -28
   
#======================================================
#Nesting level: 1 #Scope offset:28
#Parameter n Type int Pass CV Offset 12  | TemporaryVariable T@0 Datatype int Offset 16 | TemporaryVariable T@1 Datatype int Offset 20 | TemporaryVariable T@2 Datatype int Offset 24
#======================================================

   #Quad: 11 : *, n, T@1, T@2
L11: 
   lw t1, -12(sp)
   lw t2, -20(sp)
   mul t1, t1, t2
   sw t1, -24(sp)
   
#======================================================
#Nesting level: 1 #Scope offset:28
#Parameter n Type int Pass CV Offset 12  | TemporaryVariable T@0 Datatype int Offset 16 | TemporaryVariable T@1 Datatype int Offset 20 | TemporaryVariable T@2 Datatype int Offset 24
#======================================================

   #Quad: 12 : retv, T@2, _, _
L12: 
   lw t1, -24(sp)
   lw t0, -8(sp)
   sw t1, 0(t0)
   
#======================================================
#Nesting level: 1 #Scope offset:28
#Parameter n Type int Pass CV Offset 12  | TemporaryVariable T@0 Datatype int Offset 16 | TemporaryVariable T@1 Datatype int Offset 20 | TemporaryVariable T@2 Datatype int Offset 24
#======================================================

   #Quad: 13 : end_block, παραγοντικό, _, _
L13: 
   lw ra, 0(sp)
   jr ra
   
#======================================================
#Nesting level: 0 #Scope offset:24
#Variable a Datatype int Offset 12 | Variable b Datatype int Offset 16 | Function παραγοντικό, startingQuad 2, Framelength 28, Formal parameters:
#Formal parameter n, int, CV | TemporaryVariable T@3 Datatype int Offset 20
#======================================================

   #Quad: 14 : begin_block, recursiveFactorial, _, _
Lmain:

   addi sp, sp, 24
   mv gp, sp
   
#======================================================
#Nesting level: 0 #Scope offset:24
#Variable a Datatype int Offset 12 | Variable b Datatype int Offset 16 | Function παραγοντικό, startingQuad 2, Framelength 28, Formal parameters:
#Formal parameter n, int, CV | TemporaryVariable T@3 Datatype int Offset 20
#======================================================

   #Quad: 15 : :=, 5, _, b
L15: 
   li t1, 5
   sw t1, -16(sp)
   
#======================================================
#Nesting level: 0 #Scope offset:24
#Variable a Datatype int Offset 12 | Variable b Datatype int Offset 16 | Function παραγοντικό, startingQuad 2, Framelength 28, Formal parameters:
#Formal parameter n, int, CV | TemporaryVariable T@3 Datatype int Offset 20
#======================================================

   #Quad: 16 : par, b, CV, _
L16: 
   addi fp, sp, 28
   lw t0, -16(sp)
   sw t0, -12(fp)
   
#======================================================
#Nesting level: 0 #Scope offset:24
#Variable a Datatype int Offset 12 | Variable b Datatype int Offset 16 | Function παραγοντικό, startingQuad 2, Framelength 28, Formal parameters:
#Formal parameter n, int, CV | TemporaryVariable T@3 Datatype int Offset 20
#======================================================

   #Quad: 17 : par, T@3, RET, _
L17: 
   addi t0, sp, -20
   sw t0, -8(fp)
   
#======================================================
#Nesting level: 0 #Scope offset:24
#Variable a Datatype int Offset 12 | Variable b Datatype int Offset 16 | Function παραγοντικό, startingQuad 2, Framelength 28, Formal parameters:
#Formal parameter n, int, CV | TemporaryVariable T@3 Datatype int Offset 20
#======================================================

   #Quad: 18 : call, παραγοντικό, _, _
L18: 
   sw sp, -4(fp)
   addi sp, sp, 28
   jal L2
   addi sp, sp, -28
   
#======================================================
#Nesting level: 0 #Scope offset:24
#Variable a Datatype int Offset 12 | Variable b Datatype int Offset 16 | Function παραγοντικό, startingQuad 2, Framelength 28, Formal parameters:
#Formal parameter n, int, CV | TemporaryVariable T@3 Datatype int Offset 20
#======================================================

   #Quad: 19 : :=, T@3, _, a
L19: 
   lw t1, -20(sp)
   sw t1, -12(sp)
   
#======================================================
#Nesting level: 0 #Scope offset:24
#Variable a Datatype int Offset 12 | Variable b Datatype int Offset 16 | Function παραγοντικό, startingQuad 2, Framelength 28, Formal parameters:
#Formal parameter n, int, CV | TemporaryVariable T@3 Datatype int Offset 20
#======================================================

   #Quad: 20 : out, a, _, _
L20: 
   lw t1, -12(sp)
   mv  a0, t1
   li a7, 1
   ecall
   la a0, str_nl
   li a7, 4
   ecall
L21:
   li a0, 0
   li a7, 93
   ecall
