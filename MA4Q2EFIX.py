from fractions import gcd
print 'Input M1'
M10 = input()
M11 = input()
M12 = input()
print 'Input M2'
M20 = input()
M21 = input()
M22 = input()
print 'Input M3'
M30 = input()
M31 = input()
M32 = input()
MC1 = [M10,M11,M12]
MC2 = [M20,M21,M22]
MC3 = [M30,M31,M32]
MU = [MC2[0]-MC1[0],MC2[1]-MC1[1],MC2[2]-MC1[2]]
print 'M2-M1 = MU'
print MU[0]
print MU[1]
print MU[2]
MV = [MC3[0]-MC1[0],MC3[1]-MC1[1],MC3[2]-MC1[2]]
print 'M3-M1 = MV'
print MV[0]
print MV[1]
print MV[2]
MN = [MU[1]*MV[2]-MU[2]*MV[1],MU[2]*MV[0]-MU[0]*MV[2],MU[0]*MV[1]-MU[1]*MV[0]]
print 'MU Cross MV'
print MN[0]
print MN[1]
print MN[2]
print 'MN Factorise'
MA = [MN[0]/gcd(MN[0],gcd(MN[1],MN[2])),MN[1]/gcd(MN[0],gcd(MN[1],MN[2])),MN[2]/gcd(MN[0],gcd(MN[1],MN[2]))]
print MA[0]
print MA[1]
print MA[2]
