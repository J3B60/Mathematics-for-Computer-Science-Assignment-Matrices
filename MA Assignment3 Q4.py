print "Compute the determinant of a 3x3 Matrix using Laplace's Formula"
M00 = input()
M01 = input()
M02 = input()
M10 = input()
M11 = input()
M12 = input()
M20 = input()
M21 = input()
M22 = input()

M = [[M00,M01,M02],[M10,M11,M12],[M20,M21,M22]]

print M[0]
print M[1]
print M[2]

L00 = M[0][0]*(M[1][1]*M[2][2]-(M[2][1]*M[1][2]))
L01 = -1*M[0][1]*(M[1][0]*M[2][2]-(M[2][0]*M[1][2]))
L02 = M[0][2]*(M[1][0]*M[2][1]-(M[2][0]*M[1][1]))

print L00, L01, L02

AL = L00+L01+L02

print AL
