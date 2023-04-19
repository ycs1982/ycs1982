"""
Elaborar um programa que leia três valores para os lados de um triângulo,
considerando lados como A, B e C. Verificar se os lados fornecidos formam um triângulo,
e se esta condição for verdadeira, deve ser indicado o tipo de triângulo formado:
isósceles, escaleno ou equilátero. Veja o algoritmo, o diagrama de blocos e a codificação
em português estruturado, prestando atenção nos operadores lógicos.

"""


a = int(input("Lado a :"))
b = int(input("Lado b :"))
c = int(input("Lado c :"))


if a < b + c and b < c + a  and c < b + c:
    if a == b and b == c:
        print("Triangulo equilatero")
    if a != b and b != c and c != a:
        print("Triangulo escaleno")
else:
    print("isso não é um triangulo")

if not a != b and a != c:
    print ("triangulo isoceles")