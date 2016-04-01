a="1011111001000011100110101101010110011000111011110101000000000000"
b="1001110010001011011110100001010000100101001101101001100000000000"
c="1000100001010101001000100011001101100110100110011101000000000000"

u="1100100101110101101000100001001100101110100010011101000000000000"
v="1101101110011010100001100111010100110100001011111111000000000000"
w="1010011000000011100110101101010111111000110011111101100000000000"
x="1110111001010011110100101010000100111001101001001100000000000"
y="1010111110001011011011000111110101011110001111110001000000000000"

A=[]
B=[]
C=[]

U =[]
V =[]
W =[]
X =[]
Y =[]

for i in a:
    A.append(i)

for i in b:
    B.append(i)

for i in c:
    C.append(i)

for i in u:
    U.append(i)
for i in v:
    V.append(i)

for i in w:
    W.append(i)

for i in x:
    X.append(i)

for i in y:
    Y.append(i)


long = len(A)
longx = len(X)
longy = len(Y)
miss = 0
print X
print long
print longx
print longy

for x in range (0,long):
    if A[x] <> B[x]:
        miss += 1

print "distance A - B"
print "Number of non-match-bits = ",miss
print "Number of bits compared= ",long
print miss, "/" ,long ,"->", float(miss)/float(long)
miss= 0
for x in range (0,long):
    if A[x] <> C[x]:
        miss += 1

print "distance A - C"
print "Number of non-match-bits = ",miss
print "Number of bits compared= ",long
print miss, "/" ,long,"->", float(miss)/float(long)
miss= 0

for x in range (0,long):
    if C[x] <> B[x]:
        miss += 1

print "distance B - C"
print "Number of non-match-bits = ",miss
print "Number of bits compared= ",long
print miss, "/" ,long,"->", float(miss)/float(long)





###########################################################################################
print "#################     A     ###################"

for x in range (0,long):
    if A[x] <> U[x]:
        miss += 1

print "distance A - U"
print "Number of non-match-bits = ",miss
print "Number of bits compared= ",long
print miss, "/" ,long,"->", float(miss)/float(long)
miss= 0


for x in range (0,long):
    if A[x] <> V[x]:
        miss += 1

print "distance A - V"
print "Number of non-match-bits = ",miss
print "Number of bits compared= ",long
print miss, "/" ,long,"->", float(miss)/float(long)
miss= 0


for x in range (0,long):
    if A[x] <> W[x]:
        miss += 1

print "distance A - W"
print "Number of non-match-bits = ",miss
print "Number of bits compared= ",long
print miss, "/" ,long,"->", float(miss)/float(long)
miss= 0


for x in range (0,longx):
    if A[x] <> X[x]:
        miss += 1

print "distance A - X"
print "Number of non-match-bits = ",miss
print "Number of bits compared= ",long
print miss+(long-longx), "/" ,long,"->", float(miss+(long-longx))/float(long)
miss= 0


for x in range (0,longy):
    if A[x] <> Y[x]:
        miss += 1

print "distance A - Y"
print "Number of non-match-bits = ",miss
print "Number of bits compared= ",long
print miss, "/" ,long,"->", float(miss)/float(long)
miss= 0

###########################################################################################
print "#################     B     ###################"
for x in range (0,long):
    if B[x] <> U[x]:
        miss += 1

print "distance B - U"
print "Number of non-match-bits = ",miss
print "Number of bits compared= ",long
print miss, "/" ,long,"->", float(miss)/float(long)
miss= 0


for x in range (0,long):
    if B[x] <> V[x]:
        miss += 1

print "distance B - V"
print "Number of non-match-bits = ",miss
print "Number of bits compared= ",long
print miss, "/" ,long,"->", float(miss)/float(long)
miss= 0


for x in range (0,long):
    if B[x] <> W[x]:
        miss += 1

print "distance B - W"
print "Number of non-match-bits = ",miss
print "Number of bits compared= ",long
print miss, "/" ,long,"->", float(miss)/float(long)
miss= 0


for x in range (0,longx):
    if B[x] <> X[x]:
        miss += 1

print "distance B - X"
print "Number of non-match-bits = ",miss
print "Number of bits compared= ",long
print miss+(long-longx), "/" ,long,"->", float(miss+(long-longx))/float(long)
miss= 0


for x in range (0,longy):
    if B[x] <> Y[x]:
        miss += 1

print "distance B - Y"
print "Number of non-match-bits = ",miss
print "Number of bits compared= ",long
print miss, "/" ,long,"->", float(miss)/float(long)
miss= 0


###########################################################################################
print "#################     C     ###################"
for x in range (0,long):
    if C[x] <> U[x]:
        miss += 1

print "distance C - U"
print "Number of non-match-bits = ",miss
print "Number of bits compared= ",long
print miss, "/" ,long,"->", float(miss)/float(long)
miss= 0


for x in range (0,long):
    if C[x] <> V[x]:
        miss += 1

print "distance C - V"
print "Number of non-match-bits = ",miss
print "Number of bits compared= ",long
print miss, "/" ,long,"->", float(miss)/float(long)
miss= 0


for x in range (0,long):
    if C[x] <> W[x]:
        miss += 1

print "distance C - W"
print "Number of non-match-bits = ",miss
print "Number of bits compared= ",long
print miss, "/" ,long,"->", float(miss)/float(long)
miss= 0


for x in range (0,longx):
    if C[x] <> X[x]:
        miss += 1

print "distance C - X"
print "Number of non-match-bits = ",miss
print "Number of bits compared= ",long
print miss+(long-longx), "/" ,long,"->", float(miss+(long-longx))/float(long)
miss= 0


for x in range (0,longy):
    if C[x] <> Y[x]:
        miss += 1

print "distance C - Y"
print "Number of non-match-bits = ",miss
print "Number of bits compared= ",long
print miss, "/" ,long,"->", float(miss)/float(long)
miss= 0
