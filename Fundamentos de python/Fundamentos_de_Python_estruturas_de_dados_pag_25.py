def digitarNumero(prompt):
    """Essa função faz o tratamento de erro caso usuario digite algo diferente
    de um número inteiro"""
    entrada_string = input(prompt)
    try:
        numero = int(entrada_string)
        return numero
    except ValueError:
        print("Erro no formaro do numero: ",entrada_string)
        return digitarNumero(prompt)

age = digitarNumero("Entre com sua idade: ")
print("Sua idade é: ",age)