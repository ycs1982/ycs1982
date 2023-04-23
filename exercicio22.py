import random
def adivinharnumero():
    """Fornece os limites de um intervalo de números e deixa o usuário
    adivinhar o número do computador até a suposição estiver correta."""
    primeiro = int(input("Entre com o primeiro numero: "))
    ultimo = int(input("Entre com o ultimo numero: "))
    meu_numero = random.randint(primeiro,ultimo)
    contador = 0
    while True:
        contador+=1
        numero_usuario = int(input("Entre com seu numero: "))
        if numero_usuario < meu_numero:
            print("Um pouco mais")
        elif numero_usuario > meu_numero:
            print("Um pouco menos")
        else:
            print("parabens vc acertou em", contador,"tentativas")

        jogar_denovo = input("Voce deseja jogar novamente: sim ou nao?")

        if jogar_denovo != "sim":
            break

adivinharnumero()


