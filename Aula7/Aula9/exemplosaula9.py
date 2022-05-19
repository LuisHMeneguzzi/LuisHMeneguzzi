import random

#Variáveis Globais
casaPlayer1 = 0
casaPlayer2 = 0 

#Funções
def executarRegras(nJogador, nCasa):
    print('Executa as regras para o jogador', nJogador, 'que está na casa', nCasa)

def jogarDado(nJogador):
    if nJogador == 1:
        global casaPlayer1
        casaPlayer1 = casaPlayer1 + random.randint(1,6)
    else:
        casaPlayer2 = casaPlayer2 + random.randint(1,6)


def jogarDado2(casaJogador):
    novapos = casaJogador + random.randint(1,6)
    return novapos
#Código principal



#...
#a função jogarDado altera as variaveis globais
print(casaPlayer1)
jogarDado(1)
print(casaPlayer1)
jogarDado(1)
print(casaPlayer1)

#a finção jogarDado2 usa o valor passado por parametro e retorna o numero 
# da casa atualizado, que precisa ser armazenado em uma variavel
casaPlayer1 = jogarDado2(casaPlayer1)
casaPlayer2 = jogarDado2(casaPlayer2)

print(casaPlayer1)
print(casaPlayer2)
