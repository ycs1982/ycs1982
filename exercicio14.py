"""
Desenvolver um programa de computador que leia um valor numérico inteiro e faça a apresentação
desse valor caso seja divisível por 4 e 5. Não sendo divisível por 4 e 5, o programa deve
apresentar a mensagem “Valor não é divisível por 4 e 5”
"""
numero_1 = int(input("Entre com um numero: "))

if numero_1 %4 == 0 and numero_1 %5 == 0:
    print (f"Este numero{numero_1} é divisivel  por 4 e 5 ")

else:
    print(f"Esse numero {numero_1} não é divisivel por 4 e 5")