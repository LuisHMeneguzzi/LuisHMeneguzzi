arqEscrita = open('C:\\Users\\MeneguzziLuis\\Documents\\GitHub\\LuisHMeneguzzi\\Aula7\\Aula9\\lele.txt','w')

arqEscrita.write('Ola Mundo')

msg = '\nOla mundo2'

idade = 18
pi = 3.14159

arqEscrita.write(msg)
arqEscrita.write(str(idade))
arqEscrita.write(str(pi))


L = [1, 2, 3]
strL = []
for i in L:
    strL.append(str(i))

arqEscrita.writelines(strL)

arqEscrita.close()