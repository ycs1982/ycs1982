print("""Supondo que a população de um país A seja da ordem de 80000 habitantes com 
uma taxa anual de crescimento de 3% e que a população de B seja 200000 
habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule 
e escreva o número de anos necessários para que a população do país A ultrapasse 
ou iguale a população do país B, mantidas as taxas de crescimento.""")
print()

pais_a = 80000
pais_b = 200000
taxa_a = 0.03
taxa_b = 0.015

ano_inicio = 2022

while pais_a < pais_b:
    ano_inicio = ano_inicio + 1
    pais_a = pais_a + (pais_a*taxa_a)
    pais_b = pais_b + (pais_b*taxa_b)
    #print(ano_inicio,pais_a,pais_b)
print(f"o pais A alcançou a população do pais B em {ano_inicio}, com uma população de {pais_a:.2f}")
