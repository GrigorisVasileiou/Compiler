.data
   str_nl:.asciz "\n"

.text

L0: j Lmain
   
#======================================================
#Nesting level: 0 #Scope offset:44
#Variable A Datatype int Offset 12 | Variable B Datatype int Offset 16 | Variable i Datatype int Offset 20 | TemporaryVariable T@0 Datatype int Offset 24 | TemporaryVariable T@1 Datatype int Offset 28 | TemporaryVariable T@2 Datatype int Offset 32 | TemporaryVariable T@3 Datatype int Offset 36 | TemporaryVariable T@4 Datatype int Offset 40
#======================================================

   #Quad: 1 : begin_block, Προπέδια, _, _
Lmain:

   addi sp, sp, 44
   mv gp, sp
   
#======================================================
#Nesting level: 0 #Scope offset:44
#Variable A Datatype int Offset 12 | Variable B Datatype int Offset 16 | Variable i Datatype int Offset 20 | TemporaryVariable T@0 Datatype int Offset 24 | TemporaryVariable T@1 Datatype int Offset 28 | TemporaryVariable T@2 Datatype int Offset 32 | TemporaryVariable T@3 Datatype int Offset 36 | TemporaryVariable T@4 Datatype int Offset 40
#======================================================

   #Quad: 2 : :=, 1, _, A
L2: 
   li t1, 1
   sw t1, -12(sp)
   
#======================================================
#Nesting level: 0 #Scope offset:44
#Variable A Datatype int Offset 12 | Variable B Datatype int Offset 16 | Variable i Datatype int Offset 20 | TemporaryVariable T@0 Datatype int Offset 24 | TemporaryVariable T@1 Datatype int Offset 28 | TemporaryVariable T@2 Datatype int Offset 32 | TemporaryVariable T@3 Datatype int Offset 36 | TemporaryVariable T@4 Datatype int Offset 40
#======================================================

   #Quad: 3 : :=, 1, _, T@0
L3: 
   li t1, 1
   sw t1, -24(sp)
   
#======================================================
#Nesting level: 0 #Scope offset:44
#Variable A Datatype int Offset 12 | Variable B Datatype int Offset 16 | Variable i Datatype int Offset 20 | TemporaryVariable T@0 Datatype int Offset 24 | TemporaryVariable T@1 Datatype int Offset 28 | TemporaryVariable T@2 Datatype int Offset 32 | TemporaryVariable T@3 Datatype int Offset 36 | TemporaryVariable T@4 Datatype int Offset 40
#======================================================

   #Quad: 4 : >, A, 11, 6
L4: 
   lw t1, -12(sp)
   li t2, 11
   bgt t1, t2, L6
   
#======================================================
#Nesting level: 0 #Scope offset:44
#Variable A Datatype int Offset 12 | Variable B Datatype int Offset 16 | Variable i Datatype int Offset 20 | TemporaryVariable T@0 Datatype int Offset 24 | TemporaryVariable T@1 Datatype int Offset 28 | TemporaryVariable T@2 Datatype int Offset 32 | TemporaryVariable T@3 Datatype int Offset 36 | TemporaryVariable T@4 Datatype int Offset 40
#======================================================

   #Quad: 5 : jump, _, _, 7
L5: 
   j L7
   
#======================================================
#Nesting level: 0 #Scope offset:44
#Variable A Datatype int Offset 12 | Variable B Datatype int Offset 16 | Variable i Datatype int Offset 20 | TemporaryVariable T@0 Datatype int Offset 24 | TemporaryVariable T@1 Datatype int Offset 28 | TemporaryVariable T@2 Datatype int Offset 32 | TemporaryVariable T@3 Datatype int Offset 36 | TemporaryVariable T@4 Datatype int Offset 40
#======================================================

   #Quad: 6 : :=, 0, _, T@0
L6: 
   li t1, 0
   sw t1, -24(sp)
   
#======================================================
#Nesting level: 0 #Scope offset:44
#Variable A Datatype int Offset 12 | Variable B Datatype int Offset 16 | Variable i Datatype int Offset 20 | TemporaryVariable T@0 Datatype int Offset 24 | TemporaryVariable T@1 Datatype int Offset 28 | TemporaryVariable T@2 Datatype int Offset 32 | TemporaryVariable T@3 Datatype int Offset 36 | TemporaryVariable T@4 Datatype int Offset 40
#======================================================

   #Quad: 7 : =, T@0, 1, 9
L7: 
   lw t1, -24(sp)
   li t2, 1
   beq t1, t2, L9
   
#======================================================
#Nesting level: 0 #Scope offset:44
#Variable A Datatype int Offset 12 | Variable B Datatype int Offset 16 | Variable i Datatype int Offset 20 | TemporaryVariable T@0 Datatype int Offset 24 | TemporaryVariable T@1 Datatype int Offset 28 | TemporaryVariable T@2 Datatype int Offset 32 | TemporaryVariable T@3 Datatype int Offset 36 | TemporaryVariable T@4 Datatype int Offset 40
#======================================================

   #Quad: 8 : =, T@0, 0, 11
L8: 
   lw t1, -24(sp)
   li t2, 0
   beq t1, t2, L11
   
#======================================================
#Nesting level: 0 #Scope offset:44
#Variable A Datatype int Offset 12 | Variable B Datatype int Offset 16 | Variable i Datatype int Offset 20 | TemporaryVariable T@0 Datatype int Offset 24 | TemporaryVariable T@1 Datatype int Offset 28 | TemporaryVariable T@2 Datatype int Offset 32 | TemporaryVariable T@3 Datatype int Offset 36 | TemporaryVariable T@4 Datatype int Offset 40
#======================================================

   #Quad: 9 : <, A, 11, 13
L9: 
   lw t1, -12(sp)
   li t2, 11
   blt t1, t2, L13
   
#======================================================
#Nesting level: 0 #Scope offset:44
#Variable A Datatype int Offset 12 | Variable B Datatype int Offset 16 | Variable i Datatype int Offset 20 | TemporaryVariable T@0 Datatype int Offset 24 | TemporaryVariable T@1 Datatype int Offset 28 | TemporaryVariable T@2 Datatype int Offset 32 | TemporaryVariable T@3 Datatype int Offset 36 | TemporaryVariable T@4 Datatype int Offset 40
#======================================================

   #Quad: 10 : jump, _, _, 37
L10: 
   j L37
   
#======================================================
#Nesting level: 0 #Scope offset:44
#Variable A Datatype int Offset 12 | Variable B Datatype int Offset 16 | Variable i Datatype int Offset 20 | TemporaryVariable T@0 Datatype int Offset 24 | TemporaryVariable T@1 Datatype int Offset 28 | TemporaryVariable T@2 Datatype int Offset 32 | TemporaryVariable T@3 Datatype int Offset 36 | TemporaryVariable T@4 Datatype int Offset 40
#======================================================

   #Quad: 11 : >, A, 11, 13
L11: 
   lw t1, -12(sp)
   li t2, 11
   bgt t1, t2, L13
   
#======================================================
#Nesting level: 0 #Scope offset:44
#Variable A Datatype int Offset 12 | Variable B Datatype int Offset 16 | Variable i Datatype int Offset 20 | TemporaryVariable T@0 Datatype int Offset 24 | TemporaryVariable T@1 Datatype int Offset 28 | TemporaryVariable T@2 Datatype int Offset 32 | TemporaryVariable T@3 Datatype int Offset 36 | TemporaryVariable T@4 Datatype int Offset 40
#======================================================

   #Quad: 12 : jump, _, _, 37
L12: 
   j L37
   
#======================================================
#Nesting level: 0 #Scope offset:44
#Variable A Datatype int Offset 12 | Variable B Datatype int Offset 16 | Variable i Datatype int Offset 20 | TemporaryVariable T@0 Datatype int Offset 24 | TemporaryVariable T@1 Datatype int Offset 28 | TemporaryVariable T@2 Datatype int Offset 32 | TemporaryVariable T@3 Datatype int Offset 36 | TemporaryVariable T@4 Datatype int Offset 40
#======================================================

   #Quad: 13 : :=, 1, _, T@1
L13: 
   li t1, 1
   sw t1, -28(sp)
   
#======================================================
#Nesting level: 0 #Scope offset:44
#Variable A Datatype int Offset 12 | Variable B Datatype int Offset 16 | Variable i Datatype int Offset 20 | TemporaryVariable T@0 Datatype int Offset 24 | TemporaryVariable T@1 Datatype int Offset 28 | TemporaryVariable T@2 Datatype int Offset 32 | TemporaryVariable T@3 Datatype int Offset 36 | TemporaryVariable T@4 Datatype int Offset 40
#======================================================

   #Quad: 14 : :=, A, _, i
L14: 
   lw t1, -12(sp)
   sw t1, -20(sp)
   
#======================================================
#Nesting level: 0 #Scope offset:44
#Variable A Datatype int Offset 12 | Variable B Datatype int Offset 16 | Variable i Datatype int Offset 20 | TemporaryVariable T@0 Datatype int Offset 24 | TemporaryVariable T@1 Datatype int Offset 28 | TemporaryVariable T@2 Datatype int Offset 32 | TemporaryVariable T@3 Datatype int Offset 36 | TemporaryVariable T@4 Datatype int Offset 40
#======================================================

   #Quad: 15 : out, i, _, _
L15: 
   lw t1, -20(sp)
   mv  a0, t1
   li a7, 1
   ecall
   la a0, str_nl
   li a7, 4
   ecall
   
#======================================================
#Nesting level: 0 #Scope offset:44
#Variable A Datatype int Offset 12 | Variable B Datatype int Offset 16 | Variable i Datatype int Offset 20 | TemporaryVariable T@0 Datatype int Offset 24 | TemporaryVariable T@1 Datatype int Offset 28 | TemporaryVariable T@2 Datatype int Offset 32 | TemporaryVariable T@3 Datatype int Offset 36 | TemporaryVariable T@4 Datatype int Offset 40
#======================================================

   #Quad: 16 : :=, 1, _, B
L16: 
   li t1, 1
   sw t1, -16(sp)
   
#======================================================
#Nesting level: 0 #Scope offset:44
#Variable A Datatype int Offset 12 | Variable B Datatype int Offset 16 | Variable i Datatype int Offset 20 | TemporaryVariable T@0 Datatype int Offset 24 | TemporaryVariable T@1 Datatype int Offset 28 | TemporaryVariable T@2 Datatype int Offset 32 | TemporaryVariable T@3 Datatype int Offset 36 | TemporaryVariable T@4 Datatype int Offset 40
#======================================================

   #Quad: 17 : :=, 1, _, T@2
L17: 
   li t1, 1
   sw t1, -32(sp)
   
#======================================================
#Nesting level: 0 #Scope offset:44
#Variable A Datatype int Offset 12 | Variable B Datatype int Offset 16 | Variable i Datatype int Offset 20 | TemporaryVariable T@0 Datatype int Offset 24 | TemporaryVariable T@1 Datatype int Offset 28 | TemporaryVariable T@2 Datatype int Offset 32 | TemporaryVariable T@3 Datatype int Offset 36 | TemporaryVariable T@4 Datatype int Offset 40
#======================================================

   #Quad: 18 : >, B, 10, 20
L18: 
   lw t1, -16(sp)
   li t2, 10
   bgt t1, t2, L20
   
#======================================================
#Nesting level: 0 #Scope offset:44
#Variable A Datatype int Offset 12 | Variable B Datatype int Offset 16 | Variable i Datatype int Offset 20 | TemporaryVariable T@0 Datatype int Offset 24 | TemporaryVariable T@1 Datatype int Offset 28 | TemporaryVariable T@2 Datatype int Offset 32 | TemporaryVariable T@3 Datatype int Offset 36 | TemporaryVariable T@4 Datatype int Offset 40
#======================================================

   #Quad: 19 : jump, _, _, 21
L19: 
   j L21
   
#======================================================
#Nesting level: 0 #Scope offset:44
#Variable A Datatype int Offset 12 | Variable B Datatype int Offset 16 | Variable i Datatype int Offset 20 | TemporaryVariable T@0 Datatype int Offset 24 | TemporaryVariable T@1 Datatype int Offset 28 | TemporaryVariable T@2 Datatype int Offset 32 | TemporaryVariable T@3 Datatype int Offset 36 | TemporaryVariable T@4 Datatype int Offset 40
#======================================================

   #Quad: 20 : :=, 0, _, T@2
L20: 
   li t1, 0
   sw t1, -32(sp)
   
#======================================================
#Nesting level: 0 #Scope offset:44
#Variable A Datatype int Offset 12 | Variable B Datatype int Offset 16 | Variable i Datatype int Offset 20 | TemporaryVariable T@0 Datatype int Offset 24 | TemporaryVariable T@1 Datatype int Offset 28 | TemporaryVariable T@2 Datatype int Offset 32 | TemporaryVariable T@3 Datatype int Offset 36 | TemporaryVariable T@4 Datatype int Offset 40
#======================================================

   #Quad: 21 : =, T@2, 1, 23
L21: 
   lw t1, -32(sp)
   li t2, 1
   beq t1, t2, L23
   
#======================================================
#Nesting level: 0 #Scope offset:44
#Variable A Datatype int Offset 12 | Variable B Datatype int Offset 16 | Variable i Datatype int Offset 20 | TemporaryVariable T@0 Datatype int Offset 24 | TemporaryVariable T@1 Datatype int Offset 28 | TemporaryVariable T@2 Datatype int Offset 32 | TemporaryVariable T@3 Datatype int Offset 36 | TemporaryVariable T@4 Datatype int Offset 40
#======================================================

   #Quad: 22 : =, T@2, 0, 25
L22: 
   lw t1, -32(sp)
   li t2, 0
   beq t1, t2, L25
   
#======================================================
#Nesting level: 0 #Scope offset:44
#Variable A Datatype int Offset 12 | Variable B Datatype int Offset 16 | Variable i Datatype int Offset 20 | TemporaryVariable T@0 Datatype int Offset 24 | TemporaryVariable T@1 Datatype int Offset 28 | TemporaryVariable T@2 Datatype int Offset 32 | TemporaryVariable T@3 Datatype int Offset 36 | TemporaryVariable T@4 Datatype int Offset 40
#======================================================

   #Quad: 23 : <, B, 10, 27
L23: 
   lw t1, -16(sp)
   li t2, 10
   blt t1, t2, L27
   
#======================================================
#Nesting level: 0 #Scope offset:44
#Variable A Datatype int Offset 12 | Variable B Datatype int Offset 16 | Variable i Datatype int Offset 20 | TemporaryVariable T@0 Datatype int Offset 24 | TemporaryVariable T@1 Datatype int Offset 28 | TemporaryVariable T@2 Datatype int Offset 32 | TemporaryVariable T@3 Datatype int Offset 36 | TemporaryVariable T@4 Datatype int Offset 40
#======================================================

   #Quad: 24 : jump, _, _, 34
L24: 
   j L34
   
#======================================================
#Nesting level: 0 #Scope offset:44
#Variable A Datatype int Offset 12 | Variable B Datatype int Offset 16 | Variable i Datatype int Offset 20 | TemporaryVariable T@0 Datatype int Offset 24 | TemporaryVariable T@1 Datatype int Offset 28 | TemporaryVariable T@2 Datatype int Offset 32 | TemporaryVariable T@3 Datatype int Offset 36 | TemporaryVariable T@4 Datatype int Offset 40
#======================================================

   #Quad: 25 : >, B, 10, 27
L25: 
   lw t1, -16(sp)
   li t2, 10
   bgt t1, t2, L27
   
#======================================================
#Nesting level: 0 #Scope offset:44
#Variable A Datatype int Offset 12 | Variable B Datatype int Offset 16 | Variable i Datatype int Offset 20 | TemporaryVariable T@0 Datatype int Offset 24 | TemporaryVariable T@1 Datatype int Offset 28 | TemporaryVariable T@2 Datatype int Offset 32 | TemporaryVariable T@3 Datatype int Offset 36 | TemporaryVariable T@4 Datatype int Offset 40
#======================================================

   #Quad: 26 : jump, _, _, 34
L26: 
   j L34
   
#======================================================
#Nesting level: 0 #Scope offset:44
#Variable A Datatype int Offset 12 | Variable B Datatype int Offset 16 | Variable i Datatype int Offset 20 | TemporaryVariable T@0 Datatype int Offset 24 | TemporaryVariable T@1 Datatype int Offset 28 | TemporaryVariable T@2 Datatype int Offset 32 | TemporaryVariable T@3 Datatype int Offset 36 | TemporaryVariable T@4 Datatype int Offset 40
#======================================================

   #Quad: 27 : :=, 1, _, T@3
L27: 
   li t1, 1
   sw t1, -36(sp)
   
#======================================================
#Nesting level: 0 #Scope offset:44
#Variable A Datatype int Offset 12 | Variable B Datatype int Offset 16 | Variable i Datatype int Offset 20 | TemporaryVariable T@0 Datatype int Offset 24 | TemporaryVariable T@1 Datatype int Offset 28 | TemporaryVariable T@2 Datatype int Offset 32 | TemporaryVariable T@3 Datatype int Offset 36 | TemporaryVariable T@4 Datatype int Offset 40
#======================================================

   #Quad: 28 : +, i, A, T@4
L28: 
   lw t1, -20(sp)
   lw t2, -12(sp)
   add t1, t1, t2
   sw t1, -40(sp)
   
#======================================================
#Nesting level: 0 #Scope offset:44
#Variable A Datatype int Offset 12 | Variable B Datatype int Offset 16 | Variable i Datatype int Offset 20 | TemporaryVariable T@0 Datatype int Offset 24 | TemporaryVariable T@1 Datatype int Offset 28 | TemporaryVariable T@2 Datatype int Offset 32 | TemporaryVariable T@3 Datatype int Offset 36 | TemporaryVariable T@4 Datatype int Offset 40
#======================================================

   #Quad: 29 : :=, T@4, _, i
L29: 
   lw t1, -40(sp)
   sw t1, -20(sp)
   
#======================================================
#Nesting level: 0 #Scope offset:44
#Variable A Datatype int Offset 12 | Variable B Datatype int Offset 16 | Variable i Datatype int Offset 20 | TemporaryVariable T@0 Datatype int Offset 24 | TemporaryVariable T@1 Datatype int Offset 28 | TemporaryVariable T@2 Datatype int Offset 32 | TemporaryVariable T@3 Datatype int Offset 36 | TemporaryVariable T@4 Datatype int Offset 40
#======================================================

   #Quad: 30 : out, i, _, _
L30: 
   lw t1, -20(sp)
   mv  a0, t1
   li a7, 1
   ecall
   la a0, str_nl
   li a7, 4
   ecall
   
#======================================================
#Nesting level: 0 #Scope offset:44
#Variable A Datatype int Offset 12 | Variable B Datatype int Offset 16 | Variable i Datatype int Offset 20 | TemporaryVariable T@0 Datatype int Offset 24 | TemporaryVariable T@1 Datatype int Offset 28 | TemporaryVariable T@2 Datatype int Offset 32 | TemporaryVariable T@3 Datatype int Offset 36 | TemporaryVariable T@4 Datatype int Offset 40
#======================================================

   #Quad: 31 : +, T@3, B, B
L31: 
   lw t1, -36(sp)
   lw t2, -16(sp)
   add t1, t1, t2
   sw t1, -16(sp)
   
#======================================================
#Nesting level: 0 #Scope offset:44
#Variable A Datatype int Offset 12 | Variable B Datatype int Offset 16 | Variable i Datatype int Offset 20 | TemporaryVariable T@0 Datatype int Offset 24 | TemporaryVariable T@1 Datatype int Offset 28 | TemporaryVariable T@2 Datatype int Offset 32 | TemporaryVariable T@3 Datatype int Offset 36 | TemporaryVariable T@4 Datatype int Offset 40
#======================================================

   #Quad: 32 : =, T@2, 1, 23
L32: 
   lw t1, -32(sp)
   li t2, 1
   beq t1, t2, L23
   
#======================================================
#Nesting level: 0 #Scope offset:44
#Variable A Datatype int Offset 12 | Variable B Datatype int Offset 16 | Variable i Datatype int Offset 20 | TemporaryVariable T@0 Datatype int Offset 24 | TemporaryVariable T@1 Datatype int Offset 28 | TemporaryVariable T@2 Datatype int Offset 32 | TemporaryVariable T@3 Datatype int Offset 36 | TemporaryVariable T@4 Datatype int Offset 40
#======================================================

   #Quad: 33 : jump, _, _, 25
L33: 
   j L25
   
#======================================================
#Nesting level: 0 #Scope offset:44
#Variable A Datatype int Offset 12 | Variable B Datatype int Offset 16 | Variable i Datatype int Offset 20 | TemporaryVariable T@0 Datatype int Offset 24 | TemporaryVariable T@1 Datatype int Offset 28 | TemporaryVariable T@2 Datatype int Offset 32 | TemporaryVariable T@3 Datatype int Offset 36 | TemporaryVariable T@4 Datatype int Offset 40
#======================================================

   #Quad: 34 : +, T@1, A, A
L34: 
   lw t1, -28(sp)
   lw t2, -12(sp)
   add t1, t1, t2
   sw t1, -12(sp)
   
#======================================================
#Nesting level: 0 #Scope offset:44
#Variable A Datatype int Offset 12 | Variable B Datatype int Offset 16 | Variable i Datatype int Offset 20 | TemporaryVariable T@0 Datatype int Offset 24 | TemporaryVariable T@1 Datatype int Offset 28 | TemporaryVariable T@2 Datatype int Offset 32 | TemporaryVariable T@3 Datatype int Offset 36 | TemporaryVariable T@4 Datatype int Offset 40
#======================================================

   #Quad: 35 : =, T@0, 1, 9
L35: 
   lw t1, -24(sp)
   li t2, 1
   beq t1, t2, L9
   
#======================================================
#Nesting level: 0 #Scope offset:44
#Variable A Datatype int Offset 12 | Variable B Datatype int Offset 16 | Variable i Datatype int Offset 20 | TemporaryVariable T@0 Datatype int Offset 24 | TemporaryVariable T@1 Datatype int Offset 28 | TemporaryVariable T@2 Datatype int Offset 32 | TemporaryVariable T@3 Datatype int Offset 36 | TemporaryVariable T@4 Datatype int Offset 40
#======================================================

   #Quad: 36 : jump, _, _, 11
L36: 
   j L11
L37:
   li a0, 0
   li a7, 93
   ecall
