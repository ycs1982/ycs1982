print("""Obter números de um arquivo de texto no qual estão separados por espaços é um pouco mais
complicado.
Um método prossegue lendo as linhas em um laço for, como antes. Mas cada linha agora pode conter vários
números inteiros separados por espaços. Você pode usar o método de string split para obter uma lista das
strings que representam esses inteiros e, em seguida, processar cada string nesta lista com outro laço for.
O próximo segmento de código modifica o anterior para lidar com inteiros separados por espa-ços ou
novas linhas.""")

print()

f=open("Fundamentos_de_Python_estruturas_de_dados_pag_28.txt",'r')

soma = 0

for linha in f:
    lista_strings = linha.split()
    for palavra in lista_strings:
        numero = int(palavra)
        soma = soma + numero

print(f"A soma de todos os numeros é:{soma}")
f.close()

print("""Normalmente, uma boa ideia é simplificar seu código, se possível. Por exemplo, nos dois
exemplos anteriores, um laço acumula a soma de uma sequência de inteiros. O Python inclui uma função
integrada chamada sum que já faz isso. Antes de poder chamar essa função, no entanto, você deve converter
uma sequência de palavras no arquivo de entrada em uma sequência de inteiros. Você pode fazer isso sem um
laço, em quatro etapas:
1. Ler o texto do arquivo em uma única string.
2. Dividir essa string em uma lista de palavras.
3. Mapear a função int nesta lista para converter as strings em inteiros.
4. Somar o resultado.
Eis o projeto simplificado, em duas linhas de código:
f=open("integers.txt", 'r')
print("The sum is", sum(map(int, f.read (). split ())))
Como split reconhece espaços em branco ou novas linhas como separadores entre palavras,
esse código funcionará com arquivos formatados com qualquer forma de espaço em branco separando os valores
de dados.
""")