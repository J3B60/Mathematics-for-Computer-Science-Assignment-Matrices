from fractions import gcd
print"Input Matrix Values (2x3)"
M00 = input()
M01 = input()
M02 = input()
M10 = input()
M11 = input()
M12 = input()
M = [[M00,M01,M02],[M10,M11,M12]]
print ("Input Matrix Values (3x2)Assumption that N[0][1] is x")
N00 = input()
N01 = input()
N10 = input()
N11 = input()
N20 = input()
N21 = input()
N = [[N00,N01],[N10,N11],[N20,N21]]
A = [[M[0][0]*N[0][0]+M[0][1]*N[1][0]+M[0][2]*N[2][0],M[0][0]*N[0][1]+M[0][1]*N[1][1]+M[0][2]*N[2][1]],[M[1][0]*N[0][0]+M[1][1]*N[1][0]+M[1][2]*N[2][0],M[1][0]*N[0][1]+M[1][1]*N[1][1]+M[1][2]*N[2][1]]]
print A
print "X[0][1] =", M[0][0]*N[0][1]
print "X[1][1] =", M[1][0]*N[0][1]
XT1 = A[0][0]*M[1][0]*N[0][1]
NT1 = A[0][0]*(A[1][1]-M[1][0]*N[0][1])
XT2 = A[1][0]*M[0][0]*N[0][1]
NT2 = A[1][0]*(A[0][1]-M[0][0]*N[0][1])
print XT1,'x', '+', NT1, '-(',  XT2, 'x', '+', NT2, ')'
XA = XT1-XT2
NA = NT1-NT2
print XA, '+', NA
print gcd(XA, NA)
XF = XA/ gcd(XA, NA)
NF = NA/ gcd(XA, NA)
print NF, '/', -XF
