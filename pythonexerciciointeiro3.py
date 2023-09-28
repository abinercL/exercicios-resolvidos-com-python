# Solução em Python do Problema 3
# Dado um número inteiro positivo n, imprimir os n primeiros naturais ímpares
n = int(input("digite um nuemro: "))# aqui e guardado o numero inserido na variavel n 
for i in range(0, n):# a variavel n e jogada no range que entao cria o array 
    print(2 * i + 1)# esse calculo percorre todo o array para então selecionar todos os numeros n imapares 
