A = [1,2,3,4,5,6,7,8,9,10]

tamanho = len(A)

primeiro = A[0]

ultimo = A[tamanho - 1]

print('Primeiro: ', primeiro)
print('Ultimo: ', ultimo)


A = [1.1, 2.2, 3.2] # Delimitador de lista
B = ['a'] * 5 # Multiplicação de lista
C = list(range(5, 20, 3)) # Typecast de uma sequência
D = [ x**2 for x in range(1, 20) if x % 3 == 0 ] # List Comprehension
print(A)
print(B)
print(C)
print(D)