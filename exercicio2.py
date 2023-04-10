print("""Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma
lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da
média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro,
. . . ).""")

print()


lista = [ ]
mes = ["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]

for i in range(12):
    temp =float(input("Temperatura: "))
    lista.append(temp)

media = sum(lista)/12

for i in range(12):
    if lista[i]>media:
        print(f"temperatura {lista[i]} graus,mes {i+1} - {mes[i]}" )