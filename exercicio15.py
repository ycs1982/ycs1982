numero = int(input("Entre com um numero inteiro não negativo: "))

if not (numero < 0):
    if numero !=5:
        resultado = numero ** (1/2)
        print(resultado)
    else:
        resultado = numero ** (1 / 3)
        print(resultado)

if numero <=-1:
    print("operação impossivel")