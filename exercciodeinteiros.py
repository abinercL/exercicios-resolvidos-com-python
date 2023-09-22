
#Dada uma seqüência de números inteiros não-nulos, seguida por 0, imprimir seus quadrados
#soluçao do exercicio 
num = int(input("digite um numero: "))
while num != 0:
    quadrado = num*num
    print(num, "ao quadrado é", quadrado)
    num = int(input("digite um numero: "))


