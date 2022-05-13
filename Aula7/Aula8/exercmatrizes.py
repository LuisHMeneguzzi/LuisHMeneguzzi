''''
M = []

l = int(input('Digite o nro de linhas: '))
c = int(input('Digite o nro de colunas: '))

for line in range(l):
    for col in range(c):
        print(M[line][col], end="\t")
    print()
'''    

M = [
    [0, 0, 0],
    [0, 0, 0]
]

for l in range(3):
    for c in range(3):
        print(M[l][c], end="")