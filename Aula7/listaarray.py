import random
#1

A = []

for i in range(10):
    A.append(random.randint(10,90))
    
if(A == 50):
    print('Aparece o nro 50')
else:
    
    print('Não aparece o nro 50')

a0 = A[0]
a1 = A[1]
a2 = A[2]
a3 = A[3]
a4 = A[4]
a5 = A[5]
a6 = A[6]
a7 = A[7]
a8 = A[8]
a9 = A[9]

if(a0 == 50 or a1 == 50 or a2 == 50 or a3 == 50 or a4 == 50 or a5 == 50 or a6 == 50 or a7== 50 or a8 == 50  or a9 == 50):
    a0 = 1
    a1 = 1
    a2 = 1
    a3 = 1
    a4 = 1
    a5 = 1
    a6 = 1
    a7 = 1
    a8 = 1
    a9 = 1
    
    res = a0 + a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9
    print(res)

else:
    print('Nenhum nro 50')
    
    
print(A)
