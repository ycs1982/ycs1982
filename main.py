"""
Elaborar um programa que efetue a entrada de um valor numérico real não negativo diferente de cinco.
Em caso afirmativo, o programa deve calcular e exibir o resultado da raiz quadrada do valor fornecido;
caso contrário, o programa deve apresentar o resultado da raiz cúbica do valor fornecido.
Se o valor for-necido for negativo, o programa não deve executar nenhuma ação, apenas ser encerrado.

"""

numero = int(input("Entre com um numero inteiro não negativo: "))

if numero >= 0 and numero != 5:
    resultado = numero**(1/2)
    print(resultado)

if numero <=-1:
    print("operação impossivel")

else:
    resultado = numero**(1/3)
    print((resultado))