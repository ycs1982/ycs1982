print("""Gravando números em um arquivo de texto
O método de arquivo write espera uma string como argumento.
Portanto, outros tipos de dados, como inteiros ou números de ponto flutuante,
devem primeiro ser convertidos em strings antes de serem gravados em um arquivo de saída.
Em Python, os valores da maioria dos tipos de dados podem ser convertidos em strings usando o função str.
As strings resultantes são então gravadas em um arquivo com um espaço ou uma nova linha como um caractere separador.
O próximo segmento de código ilustra a saída de inteiros para um arquivo de texto.
Quinhentos inteiros aleatórios entre 1 e 500 são gerados e gravados em um arquivo de texto 
denominado integers.txt. O caractere de nova linha é o separador.
""")


import random

f=open("Fundamentos_de_Python_estruturas_de_dados_pag_28.txt",'w')

for i in range(20):
    numero = random.randint(0,20)
    f.write(str(numero) + "\n")

f.close()

