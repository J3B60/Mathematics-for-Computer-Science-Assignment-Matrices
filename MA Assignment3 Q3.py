print 'Compute the adjoint of a 3x3 Matrix'
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

print M

C00 = M[1][1]*M[2][2]-(M[2][1]*M[1][2])
C01 = -1*(M[1][0]*M[2][2]-(M[2][0]*M[1][2]))
C02 = M[1][0]*M[2][1]-(M[2][0]*M[1][1])

C10 = -1*M[0][1]*M[2][2]-(M[2][1]*M[0][2])
C11 = (M[0][0]*M[2][2]-(M[2][0]*M[0][2]))
C12 = -1*M[0][0]*M[2][1]-(M[2][0]*M[0][1])

C20 = M[0][1]*M[1][2]-(M[1][1]*M[0][2])
C21 = -1*(M[0][0]*M[1][2]-(M[1][0]*M[0][2]))
C22 = M[0][0]*M[1][1]-(M[1][0]*M[0][1])

C = [[C00,C01,C02],[C10,C11,C12],[C20,C21,C22]]

print C

CT = [[C00,C10,C20],[C01,C11,C21],[C02,C12,C22]]

print CT
