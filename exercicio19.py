"""
Elaborar um programa que efetue a entrada de um valor numérico inteiro qualquer.
Em seguida, cal-cular o valor entrado, multiplicando-o por 3 e apresentando seu resultado.
Ao final da apresentação do resultado, o programa deve perguntar ao usuário se ele deseja
novo cálculo. Se a resposta for sim, deve executar novamente as instruções subordinadas ao
bloco adjacente. Se a resposta for não, o programa deve parar a execução
"""
x = int(input("Entre com um valor acima de zero: "))

while True:
    resultado = x * 3
    print(resultado)
