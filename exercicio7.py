import random

palavras = [ "teste", "coração", "amor", "paz", "mansidão"]

palavra = random.choice(palavras)

letras = list(palavra)

for i in range(len(letras)):
    letras[i] = "-"


tentativas = 0

while True:
    print("".join(letras))

    tentativa = input("Digite uma letra: ")

    tentativas+=1

    if tentativa in palavra:
        for i in range(len(palavra)):
            if palavra[i] == tentativa:
                letras[i] = tentativa
    else:
        print("A letra", tentativa, "não está na palavra.")

    if "-" not in letras:
        print("Parabéns, você ganhou!")
        break

    if tentativas == 6:
        print("Você perdeu! A palavra era", palavra)
        break

