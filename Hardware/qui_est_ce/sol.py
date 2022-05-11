from z3 import *

#
# We're going to use z3 SMT solver to solve the circuit ant get back to input [x62..x0] from provided output [y62..y0]
# First time I'm using z3, so I've used a collection of variables. Maybe an array or list was possible. Oh well..
#

# Given ouput [y0..y62]
y__ = [1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1]

# Revert the output to get [y62..y0], i.e. y0=LSB and y62=MSB
y_ = y__[::-1]

# Use z3 Bool variables, so change 1 to True and 0 to False...
y = y_
for i in range(len(y_)):
    if y_[i] == 1:
        y[i] = True
    else:
        y[i] = False

# Declare the collection of input variables x0..x62
x0 = Bool('x0')
x1 = Bool('x1')
x2 = Bool('x2')
x3 = Bool('x3')
x4 = Bool('x4')
x5 = Bool('x5')
x6 = Bool('x6')
x7 = Bool('x7')
x8 = Bool('x8')
x9 = Bool('x9')
x10 = Bool('x10')
x11 = Bool('x11')
x12 = Bool('x12')
x13 = Bool('x13')
x14 = Bool('x14')
x15 = Bool('x15')
x16 = Bool('x16')
x17 = Bool('x17')
x18 = Bool('x18')
x19 = Bool('x19')
x20 = Bool('x20')
x21 = Bool('x21')
x22 = Bool('x22')
x23 = Bool('x23')
x24 = Bool('x24')
x25 = Bool('x25')
x26 = Bool('x26')
x27 = Bool('x27')
x28 = Bool('x28')
x29 = Bool('x29')
x30 = Bool('x30')
x31 = Bool('x31')
x32 = Bool('x32')
x33 = Bool('x33')
x34 = Bool('x34')
x35 = Bool('x35')
x36 = Bool('x36')
x37 = Bool('x37')
x38 = Bool('x38')
x39 = Bool('x39')
x40 = Bool('x40')
x41 = Bool('x41')
x42 = Bool('x42')
x43 = Bool('x43')
x44 = Bool('x44')
x45 = Bool('x45')
x46 = Bool('x46')
x47 = Bool('x47')
x48 = Bool('x48')
x49 = Bool('x49')
x50 = Bool('x50')
x51 = Bool('x51')
x52 = Bool('x52')
x53 = Bool('x53')
x54 = Bool('x54')
x55 = Bool('x55')
x56 = Bool('x56')
x57 = Bool('x57')
x58 = Bool('x58')
x59 = Bool('x59')
x60 = Bool('x60')
x61 = Bool('x61')
x62 = Bool('x62')

# Create the SMT solver instance and feed it with constraints giving output y0..y62 as a (Boolean) expression of input x0..x62
s = Solver()
s.add(
Xor(x0,  And(x61, Not(x62))) == y[0],
Xor(x1,  And(x62, Not(x0)))  == y[1],
Xor(x2,  And(x0,  Not(x1)))  == y[2],
Xor(x3,  And(x1,  Not(x2)))  == y[3],
Xor(x4,  And(x2,  Not(x3)))  == y[4],
Xor(x5,  And(x3,  Not(x4)))  == y[5],
Xor(x6,  And(x4,  Not(x5)))  == y[6],
Xor(x7,  And(x5,  Not(x6)))  == y[7],
Xor(x8,  And(x6,  Not(x7)))  == y[8],
Xor(x9,  And(x7,  Not(x8)))  == y[9],
Xor(x10, And(x8,  Not(x9)))  == y[10],
Xor(x11, And(x9,  Not(x10))) == y[11],
Xor(x12, And(x10, Not(x11))) == y[12],
Xor(x13, And(x11, Not(x12))) == y[13],
Xor(x14, And(x12, Not(x13))) == y[14],
Xor(x15, And(x13, Not(x14))) == y[15],
Xor(x16, And(x14, Not(x15))) == y[16],
Xor(x17, And(x15, Not(x16))) == y[17],
Xor(x18, And(x16, Not(x17))) == y[18],
Xor(x19, And(x17, Not(x18))) == y[19],
Xor(x20, And(x18, Not(x19))) == y[20],
Xor(x21, And(x19, Not(x20))) == y[21],
Xor(x22, And(x20, Not(x21))) == y[22],
Xor(x23, And(x21, Not(x22))) == y[23],
Xor(x24, And(x22, Not(x23))) == y[24],
Xor(x25, And(x23, Not(x24))) == y[25],
Xor(x26, And(x24, Not(x25))) == y[26],
Xor(x27, And(x25, Not(x26))) == y[27],
Xor(x28, And(x26, Not(x27))) == y[28],
Xor(x29, And(x27, Not(x28))) == y[29],
Xor(x30, And(x28, Not(x29))) == y[30],
Xor(x31, And(x29, Not(x30))) == y[31],
Xor(x32, And(x30, Not(x31))) == y[32],
Xor(x33, And(x31, Not(x32))) == y[33],
Xor(x34, And(x32, Not(x33))) == y[34],
Xor(x35, And(x33, Not(x34))) == y[35],
Xor(x36, And(x34, Not(x35))) == y[36],
Xor(x37, And(x35, Not(x36))) == y[37],
Xor(x38, And(x36, Not(x37))) == y[38],
Xor(x39, And(x37, Not(x38))) == y[39],
Xor(x40, And(x38, Not(x39))) == y[40],
Xor(x41, And(x39, Not(x40))) == y[41],
Xor(x42, And(x40, Not(x41))) == y[42],
Xor(x43, And(x41, Not(x42))) == y[43],
Xor(x44, And(x42, Not(x43))) == y[44],
Xor(x45, And(x43, Not(x44))) == y[45],
Xor(x46, And(x44, Not(x45))) == y[46],
Xor(x47, And(x45, Not(x46))) == y[47],
Xor(x48, And(x46, Not(x47))) == y[48],
Xor(x49, And(x47, Not(x48))) == y[49],
Xor(x50, And(x48, Not(x49))) == y[50],
Xor(x51, And(x49, Not(x50))) == y[51],
Xor(x52, And(x50, Not(x51))) == y[52],
Xor(x53, And(x51, Not(x52))) == y[53],
Xor(x54, And(x52, Not(x53))) == y[54],
Xor(x55, And(x53, Not(x54))) == y[55],
Xor(x56, And(x54, Not(x55))) == y[56],
Xor(x57, And(x55, Not(x56))) == y[57],
Xor(x58, And(x56, Not(x57))) == y[58],
Xor(x59, And(x57, Not(x58))) == y[59],
Xor(x60, And(x58, Not(x59))) == y[60],
Xor(x61, And(x59, Not(x60))) == y[61],
Xor(x62, And(x60, Not(x61))) == y[62],
)
s.check()

# Solve it !!
m = s.model()

# Retrieve the inputs xO..x62 from the solver solution
# Again, it's maybe possible to use array, but oh well..
sol = y
sol[0] = m[x0]
sol[1] = m[x1]
sol[2] = m[x2]
sol[3] = m[x3]
sol[4] = m[x4]
sol[5] = m[x5]
sol[6] = m[x6]
sol[7] = m[x7]
sol[8] = m[x8]
sol[9] = m[x9]
sol[10] = m[x10]
sol[11] = m[x11]
sol[12] = m[x12]
sol[13] = m[x13]
sol[14] = m[x14]
sol[15] = m[x15]
sol[16] = m[x16]
sol[17] = m[x17]
sol[18] = m[x18]
sol[19] = m[x19]
sol[20] = m[x20]
sol[21] = m[x21]
sol[22] = m[x22]
sol[23] = m[x23]
sol[24] = m[x24]
sol[25] = m[x25]
sol[26] = m[x26]
sol[27] = m[x27]
sol[28] = m[x28]
sol[29] = m[x29]
sol[30] = m[x30]
sol[31] = m[x31]
sol[32] = m[x32]
sol[33] = m[x33]
sol[34] = m[x34]
sol[35] = m[x35]
sol[36] = m[x36]
sol[37] = m[x37]
sol[38] = m[x38]
sol[39] = m[x39]
sol[40] = m[x40]
sol[41] = m[x41]
sol[42] = m[x42]
sol[43] = m[x43]
sol[44] = m[x44]
sol[45] = m[x45]
sol[46] = m[x46]
sol[47] = m[x47]
sol[48] = m[x48]
sol[49] = m[x49]
sol[50] = m[x50]
sol[51] = m[x51]
sol[52] = m[x52]
sol[53] = m[x53]
sol[54] = m[x54]
sol[55] = m[x55]
sol[56] = m[x56]
sol[57] = m[x57]
sol[58] = m[x58]
sol[59] = m[x59]
sol[60] = m[x60]
sol[61] = m[x61]
sol[62] = m[x62]

# Change back the solution inpout x0..x62 from Booleans to 1s and 0s:
sol_ = ""
for i in range(len(sol)):
    if sol[i] == True:
        sol_ += "1"
    else:
        sol_ += "0"

# Finally revert and get the flag as a decimal:
val = int(sol_[::-1], 2)
tag = "FCSC{" + str(val) + "}"
print(tag)

# FCSC{7364529468137835333}
