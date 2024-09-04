import math
import os

repetir = True

def fib(x):
    positivo = (5 * x * x + 4)
    negativo = (5 * x * x - 4)


    s1 = int(math.sqrt(positivo))
    s2 = int(math.sqrt(negativo))
    if s1 * s1 == positivo or s2 * s2 == negativo:
        return f'o numero {x} está na sequencia de Fibonacci.'
    else:
        return f'o numero {x} não está na sequencia de Fibonacci.'

while repetir:
    os.system('cls')
    N = int(input('Insira o Numero a ser checado. \n'))
    print(fib(N))
    resposta = input('deseja continuar? S/N \n')
    if resposta.upper() == 'S':
        repetir = True
    else:
        repetir = False