"""
Elaborar um programa que efetue a entrada de um valor numérico inteiro qualquer.
Em seguida, cal-cular o valor entrado, multiplicando-o por 3 e apresentando seu resultado.
Proceder à execução dos passos anteriores cinco vezes.
"""
resp = 0

while resp < 5:
    x = int(input("Entre com um valor acima de zero: "))
    resultado = x * 3
    print(resultado)
    resp+=1

