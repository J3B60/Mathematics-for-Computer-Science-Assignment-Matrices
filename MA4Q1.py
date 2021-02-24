print 'Input M1'
M10 = input()
M11 = input()
M12 = input()
print 'Input M2'
M20 = input()
M21 = input()
M22 = input()
MC1 = [M10,M11,M12]
MC2 = [M20,M21,M22]

A = (MC1[0]*MC2[0]) + (MC1[1]*MC2[1]) + (MC1[2]*MC2[2])
print 'M1 Dot M2 =', A
