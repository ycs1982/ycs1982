print("""Desenvolva um programa que faça a tabuada de um número qualquer inteiro 
que será digitado pelo usuário, mas a tabuada não deve necessariamente 
iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados 
também pelo usuário, conforme exemplo abaixo:
""")

print()

while True:
    d = float(input("Montar a tabuada de: "))
    a = float(input("Começar por: "))
    b = float(input("Terminar em: "))
    if b < a:
        print("erro")

    else:
        for i in range(a,b):
            c = d * i
            print(f"{d} x {i} = {c}")
    break



