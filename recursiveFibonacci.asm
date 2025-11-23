.data
   str_nl:.asciz "\n"

.text

L0: j Lmain
   
#======================================================
#Nesting level: 1 #Scope offset:36
#Parameter x Type int Pass CV Offset 12  | TemporaryVariable T@0 Datatype int Offset 16 | TemporaryVariable T@1 Datatype int Offset 20 | TemporaryVariable T@2 Datatype int Offset 24 | TemporaryVariable T@3 Datatype int Offset 28 | TemporaryVariable T@4 Datatype int Offset 32
#======================================================

   #Quad: 1 : begin_block, Φιμπονάτσι, _, _
L1: 
   
#======================================================
#Nesting level: 1 #Scope offset:36
#Parameter x Type int Pass CV Offset 12  | TemporaryVariable T@0 Datatype int Offset 16 | TemporaryVariable T@1 Datatype int Offset 20 | TemporaryVariable T@2 Datatype int Offset 24 | TemporaryVariable T@3 Datatype int Offset 28 | TemporaryVariable T@4 Datatype int Offset 32
#======================================================

   #Quad: 2 : out, x, _, _
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
#Nesting level: 1 #Scope offset:36
#Parameter x Type int Pass CV Offset 12  | TemporaryVariable T@0 Datatype int Offset 16 | TemporaryVariable T@1 Datatype int Offset 20 | TemporaryVariable T@2 Datatype int Offset 24 | TemporaryVariable T@3 Datatype int Offset 28 | TemporaryVariable T@4 Datatype int Offset 32
#======================================================

   #Quad: 3 : <=, x, 0, 5
L3: 
   lw t1, -12(sp)
   li t2, 0
   ble t1, t2, L5
   
#======================================================
#Nesting level: 1 #Scope offset:36
#Parameter x Type int Pass CV Offset 12  | TemporaryVariable T@0 Datatype int Offset 16 | TemporaryVariable T@1 Datatype int Offset 20 | TemporaryVariable T@2 Datatype int Offset 24 | TemporaryVariable T@3 Datatype int Offset 28 | TemporaryVariable T@4 Datatype int Offset 32
#======================================================

   #Quad: 4 : jump, _, _, 7
L4: 
   j L7
   
#======================================================
#Nesting level: 1 #Scope offset:36
#Parameter x Type int Pass CV Offset 12  | TemporaryVariable T@0 Datatype int Offset 16 | TemporaryVariable T@1 Datatype int Offset 20 | TemporaryVariable T@2 Datatype int Offset 24 | TemporaryVariable T@3 Datatype int Offset 28 | TemporaryVariable T@4 Datatype int Offset 32
#======================================================

   #Quad: 5 : retv, 0, _, _
L5: 
   li t1, 0
   lw t0, -8(sp)
   sw t1, 0(t0)
   
#======================================================
#Nesting level: 1 #Scope offset:36
#Parameter x Type int Pass CV Offset 12  | TemporaryVariable T@0 Datatype int Offset 16 | TemporaryVariable T@1 Datatype int Offset 20 | TemporaryVariable T@2 Datatype int Offset 24 | TemporaryVariable T@3 Datatype int Offset 28 | TemporaryVariable T@4 Datatype int Offset 32
#======================================================

   #Quad: 6 : jump, _, _, 21
L6: 
   j L21
   
#======================================================
#Nesting level: 1 #Scope offset:36
#Parameter x Type int Pass CV Offset 12  | TemporaryVariable T@0 Datatype int Offset 16 | TemporaryVariable T@1 Datatype int Offset 20 | TemporaryVariable T@2 Datatype int Offset 24 | TemporaryVariable T@3 Datatype int Offset 28 | TemporaryVariable T@4 Datatype int Offset 32
#======================================================

   #Quad: 7 : =, x, 1, 9
L7: 
   lw t1, -12(sp)
   li t2, 1
   beq t1, t2, L9
   
#======================================================
#Nesting level: 1 #Scope offset:36
#Parameter x Type int Pass CV Offset 12  | TemporaryVariable T@0 Datatype int Offset 16 | TemporaryVariable T@1 Datatype int Offset 20 | TemporaryVariable T@2 Datatype int Offset 24 | TemporaryVariable T@3 Datatype int Offset 28 | TemporaryVariable T@4 Datatype int Offset 32
#======================================================

   #Quad: 8 : jump, _, _, 11
L8: 
   j L11
   
#======================================================
#Nesting level: 1 #Scope offset:36
#Parameter x Type int Pass CV Offset 12  | TemporaryVariable T@0 Datatype int Offset 16 | TemporaryVariable T@1 Datatype int Offset 20 | TemporaryVariable T@2 Datatype int Offset 24 | TemporaryVariable T@3 Datatype int Offset 28 | TemporaryVariable T@4 Datatype int Offset 32
#======================================================

   #Quad: 9 : retv, 1, _, _
L9: 
   li t1, 1
   lw t0, -8(sp)
   sw t1, 0(t0)
   
#======================================================
#Nesting level: 1 #Scope offset:36
#Parameter x Type int Pass CV Offset 12  | TemporaryVariable T@0 Datatype int Offset 16 | TemporaryVariable T@1 Datatype int Offset 20 | TemporaryVariable T@2 Datatype int Offset 24 | TemporaryVariable T@3 Datatype int Offset 28 | TemporaryVariable T@4 Datatype int Offset 32
#======================================================

   #Quad: 10 : jump, _, _, 21
L10: 
   j L21
   
#======================================================
#Nesting level: 1 #Scope offset:36
#Parameter x Type int Pass CV Offset 12  | TemporaryVariable T@0 Datatype int Offset 16 | TemporaryVariable T@1 Datatype int Offset 20 | TemporaryVariable T@2 Datatype int Offset 24 | TemporaryVariable T@3 Datatype int Offset 28 | TemporaryVariable T@4 Datatype int Offset 32
#======================================================

   #Quad: 11 : -, x, 1, T@0
L11: 
   lw t1, -12(sp)
   li t2, 1
   sub t1, t1, t2
   sw t1, -16(sp)
   
#======================================================
#Nesting level: 1 #Scope offset:36
#Parameter x Type int Pass CV Offset 12  | TemporaryVariable T@0 Datatype int Offset 16 | TemporaryVariable T@1 Datatype int Offset 20 | TemporaryVariable T@2 Datatype int Offset 24 | TemporaryVariable T@3 Datatype int Offset 28 | TemporaryVariable T@4 Datatype int Offset 32
#======================================================

   #Quad: 12 : par, T@0, CV, _
L12: 
   addi fp, sp, 36
   lw t0, -16(sp)
   sw t0, -12(fp)
   
#======================================================
#Nesting level: 1 #Scope offset:36
#Parameter x Type int Pass CV Offset 12  | TemporaryVariable T@0 Datatype int Offset 16 | TemporaryVariable T@1 Datatype int Offset 20 | TemporaryVariable T@2 Datatype int Offset 24 | TemporaryVariable T@3 Datatype int Offset 28 | TemporaryVariable T@4 Datatype int Offset 32
#======================================================

   #Quad: 13 : par, T@1, RET, _
L13: 
   addi t0, sp, -20
   sw t0, -8(fp)
   
#======================================================
#Nesting level: 1 #Scope offset:36
#Parameter x Type int Pass CV Offset 12  | TemporaryVariable T@0 Datatype int Offset 16 | TemporaryVariable T@1 Datatype int Offset 20 | TemporaryVariable T@2 Datatype int Offset 24 | TemporaryVariable T@3 Datatype int Offset 28 | TemporaryVariable T@4 Datatype int Offset 32
#======================================================

   #Quad: 14 : call, Φιμπονάτσι, _, _
L14: 
   lw t0, -4(sp)
   sw t0, -4(fp)
   addi sp, sp, 36
   jal L2
   addi sp, sp, -36
   
#======================================================
#Nesting level: 1 #Scope offset:36
#Parameter x Type int Pass CV Offset 12  | TemporaryVariable T@0 Datatype int Offset 16 | TemporaryVariable T@1 Datatype int Offset 20 | TemporaryVariable T@2 Datatype int Offset 24 | TemporaryVariable T@3 Datatype int Offset 28 | TemporaryVariable T@4 Datatype int Offset 32
#======================================================

   #Quad: 15 : -, x, 2, T@2
L15: 
   lw t1, -12(sp)
   li t2, 2
   sub t1, t1, t2
   sw t1, -24(sp)
   
#======================================================
#Nesting level: 1 #Scope offset:36
#Parameter x Type int Pass CV Offset 12  | TemporaryVariable T@0 Datatype int Offset 16 | TemporaryVariable T@1 Datatype int Offset 20 | TemporaryVariable T@2 Datatype int Offset 24 | TemporaryVariable T@3 Datatype int Offset 28 | TemporaryVariable T@4 Datatype int Offset 32
#======================================================

   #Quad: 16 : par, T@2, CV, _
L16: 
   addi fp, sp, 36
   lw t0, -24(sp)
   sw t0, -12(fp)
   
#======================================================
#Nesting level: 1 #Scope offset:36
#Parameter x Type int Pass CV Offset 12  | TemporaryVariable T@0 Datatype int Offset 16 | TemporaryVariable T@1 Datatype int Offset 20 | TemporaryVariable T@2 Datatype int Offset 24 | TemporaryVariable T@3 Datatype int Offset 28 | TemporaryVariable T@4 Datatype int Offset 32
#======================================================

   #Quad: 17 : par, T@3, RET, _
L17: 
   addi t0, sp, -28
   sw t0, -8(fp)
   
#======================================================
#Nesting level: 1 #Scope offset:36
#Parameter x Type int Pass CV Offset 12  | TemporaryVariable T@0 Datatype int Offset 16 | TemporaryVariable T@1 Datatype int Offset 20 | TemporaryVariable T@2 Datatype int Offset 24 | TemporaryVariable T@3 Datatype int Offset 28 | TemporaryVariable T@4 Datatype int Offset 32
#======================================================

   #Quad: 18 : call, Φιμπονάτσι, _, _
L18: 
   lw t0, -4(sp)
   sw t0, -4(fp)
   addi sp, sp, 36
   jal L2
   addi sp, sp, -36
   
#======================================================
#Nesting level: 1 #Scope offset:36
#Parameter x Type int Pass CV Offset 12  | TemporaryVariable T@0 Datatype int Offset 16 | TemporaryVariable T@1 Datatype int Offset 20 | TemporaryVariable T@2 Datatype int Offset 24 | TemporaryVariable T@3 Datatype int Offset 28 | TemporaryVariable T@4 Datatype int Offset 32
#======================================================

   #Quad: 19 : +, T@1, T@3, T@4
L19: 
   lw t1, -20(sp)
   lw t2, -28(sp)
   add t1, t1, t2
   sw t1, -32(sp)
   
#======================================================
#Nesting level: 1 #Scope offset:36
#Parameter x Type int Pass CV Offset 12  | TemporaryVariable T@0 Datatype int Offset 16 | TemporaryVariable T@1 Datatype int Offset 20 | TemporaryVariable T@2 Datatype int Offset 24 | TemporaryVariable T@3 Datatype int Offset 28 | TemporaryVariable T@4 Datatype int Offset 32
#======================================================

   #Quad: 20 : retv, T@4, _, _
L20: 
   lw t1, -32(sp)
   lw t0, -8(sp)
   sw t1, 0(t0)
   
#======================================================
#Nesting level: 1 #Scope offset:36
#Parameter x Type int Pass CV Offset 12  | TemporaryVariable T@0 Datatype int Offset 16 | TemporaryVariable T@1 Datatype int Offset 20 | TemporaryVariable T@2 Datatype int Offset 24 | TemporaryVariable T@3 Datatype int Offset 28 | TemporaryVariable T@4 Datatype int Offset 32
#======================================================

   #Quad: 21 : end_block, Φιμπονάτσι, _, _
L21: 
   lw ra, 0(sp)
   jr ra
   
#======================================================
#Nesting level: 0 #Scope offset:24
#Variable y Datatype int Offset 12 | Variable p Datatype int Offset 16 | Function Φιμπονάτσι, startingQuad 2, Framelength 36, Formal parameters:
#Formal parameter x, int, CV | TemporaryVariable T@5 Datatype int Offset 20
#======================================================

   #Quad: 22 : begin_block, αναδρομικόΦιμπονάτσι, _, _
Lmain:

   addi sp, sp, 24
   mv gp, sp
   
#======================================================
#Nesting level: 0 #Scope offset:24
#Variable y Datatype int Offset 12 | Variable p Datatype int Offset 16 | Function Φιμπονάτσι, startingQuad 2, Framelength 36, Formal parameters:
#Formal parameter x, int, CV | TemporaryVariable T@5 Datatype int Offset 20
#======================================================

   #Quad: 23 : in, p, _, _
L23: 
   li a7, 5
   ecall
   mv t0, a0
   sw t0, -16(sp)
   la a0, str_nl
   li a7, 4
   ecall
   
#======================================================
#Nesting level: 0 #Scope offset:24
#Variable y Datatype int Offset 12 | Variable p Datatype int Offset 16 | Function Φιμπονάτσι, startingQuad 2, Framelength 36, Formal parameters:
#Formal parameter x, int, CV | TemporaryVariable T@5 Datatype int Offset 20
#======================================================

   #Quad: 24 : par, p, CV, _
L24: 
   addi fp, sp, 36
   lw t0, -16(sp)
   sw t0, -12(fp)
   
#======================================================
#Nesting level: 0 #Scope offset:24
#Variable y Datatype int Offset 12 | Variable p Datatype int Offset 16 | Function Φιμπονάτσι, startingQuad 2, Framelength 36, Formal parameters:
#Formal parameter x, int, CV | TemporaryVariable T@5 Datatype int Offset 20
#======================================================

   #Quad: 25 : par, T@5, RET, _
L25: 
   addi t0, sp, -20
   sw t0, -8(fp)
   
#======================================================
#Nesting level: 0 #Scope offset:24
#Variable y Datatype int Offset 12 | Variable p Datatype int Offset 16 | Function Φιμπονάτσι, startingQuad 2, Framelength 36, Formal parameters:
#Formal parameter x, int, CV | TemporaryVariable T@5 Datatype int Offset 20
#======================================================

   #Quad: 26 : call, Φιμπονάτσι, _, _
L26: 
   sw sp, -4(fp)
   addi sp, sp, 36
   jal L2
   addi sp, sp, -36
   
#======================================================
#Nesting level: 0 #Scope offset:24
#Variable y Datatype int Offset 12 | Variable p Datatype int Offset 16 | Function Φιμπονάτσι, startingQuad 2, Framelength 36, Formal parameters:
#Formal parameter x, int, CV | TemporaryVariable T@5 Datatype int Offset 20
#======================================================

   #Quad: 27 : :=, T@5, _, y
L27: 
   lw t1, -20(sp)
   sw t1, -12(sp)
   
#======================================================
#Nesting level: 0 #Scope offset:24
#Variable y Datatype int Offset 12 | Variable p Datatype int Offset 16 | Function Φιμπονάτσι, startingQuad 2, Framelength 36, Formal parameters:
#Formal parameter x, int, CV | TemporaryVariable T@5 Datatype int Offset 20
#======================================================

   #Quad: 28 : out, y, _, _
L28: 
   lw t1, -12(sp)
   mv  a0, t1
   li a7, 1
   ecall
   la a0, str_nl
   li a7, 4
   ecall
L29:
   li a0, 0
   li a7, 93
   ecall
