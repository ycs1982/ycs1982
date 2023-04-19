"""
Elaborar um programa que leia um valor inteiro qualquer e apresente esse valor somente se
for divi-sível por 2 ou somente se for divisível 3. Caso contrário, não faça nada.
Em nenhuma hipótese esse valor pode ser apresentado caso seja divisível por 2 e/ou 3
"""
x = int(input("Entre com um valor inteiro acima de 0: "))

if x %2 == 0 and x %3 == 0:
    print(x,"é divisivel por 2 e 3")
