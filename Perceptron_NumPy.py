# 02 - Implementação do Perceptron com NUMPY

import numpy as np

entradas = np.array([-1, 7, 5]) #Criando um array do Numpy para nao ser apenas um simples vetor, se não não funciona
pesos = np.array([0.8, 0.1, 0])  # Os pesos também podem ser chamados de snapses


# Criar uma função soma
def soma(e, p):
    return e.dot(p)# dot product / Produto Escalar - Ja faz a multiplicação e a soma
    '''
    s = 0
    for i in range(3):
        # print(entradas[i])
        # print(pesos[i])
        s += e[i] * p[i]  # Faz a somatória dentro do FOR (e*i + e*i + e*i)
    return s
    '''

s = soma(entradas, pesos)
print('O Valor de S é: {}'.format(s))

# CRIADO A STEP FUNCTION
def stepFunction(soma):
    if (soma >= 1):
        return 1
    return 0

# CRIANDO A VARIÁVEL DE RESULTADO
r = stepFunction(s) # Retorna o valor 1 ou 0
print('O Valor de R é: {}'.format(r))
