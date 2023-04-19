"""
Elaborar um programa que efetue a entrada de um valor numérico inteiro qualquer.
Em seguida, pro-cessar o cálculo do valor de entrada, multiplicando-o por 3 e apresentando
seu resultado. Proceder à execução dos passos anteriores cinco vezes.
"""

x = int(input("Entre com um valor acima de 0: "))

contador = 0

while contador < 5:
    resultado = x * 3
    print(resultado)
    contador+=1