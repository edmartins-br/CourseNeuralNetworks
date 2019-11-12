import numpy as np

#entradas = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
#aidas = np.array([0, 0, 0, 1])

#Agora a rede neural será treinada para aprender qual o melhor conjunto depesos para atingir os novos valores de sauda considerados com ometa

#OPERADOR OR
#entradas = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
#saidas = np.array([0, 1, 1, 1])

#OPERADOR XOR - NÃO É MUITO UTILIZADO E NÃO DA CERTO PARA ESTE PROBLEMA - NÃO VAI CONSEGUIR ENCONTRAR O PADRÃO NESSE OPERADOR LOGICO shor
entradas = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
saidas = np.array([0, 0, 0, 1])
pesos = np.array([0.0, 0.0])  # Precisa ser 0.0 e nao soemnte zero
taxaAprendizagem = 0.1


def stepFunction(soma):
    if (soma >= 1):
        return 1
    return 0


def calculaSaida(registro):
    s = registro.dot(pesos)
    return stepFunction(s)  # retorna 1 ou 0 de acordo com o valor definido na stepFunction


def treinar():
    erroTotal = 1
    while (erroTotal != 0):
        erroTotal = 0
        for i in range(len(saidas)):
            saidaCalculada = calculaSaida(np.asarray(entradas[i]))
            erro = abs(saidas[
                           i] - saidaCalculada)  # ABS serve para que não faça diferenca colocar o saidaCalculada antes e dar o valor errado, pra nao ficar ocm o valor negativo
            erroTotal += erro
            for j in range(len(pesos)):
                pesos[j] = (pesos[j] + taxaAprendizagem * entradas[i][j] * erro)
                print('Peso atualizado: ' + str(pesos[j]))
        print('Total de erros: ' + str(erroTotal))


treinar()
print('Rede neural treinada!')
print('Saida 01 calculada: {}'.format(calculaSaida(entradas[0])))
print('Saida 02 calculada: {}'.format(calculaSaida(entradas[1])))
print('Saida 03 calculada: {}'.format(calculaSaida(entradas[2])))
print('Saida 04 calculada: {}'.format(calculaSaida(entradas[3])))
