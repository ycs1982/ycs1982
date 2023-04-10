print("""Lendo números de um arquivo
Todas as operações de entrada de arquivo retornam dados ao programa como strings. 
Se essas strings representam outros tipos de dados, como inteiros ou números de ponto flu-tuante,
o programador deve convertê-las nos tipos apropriados antes de manipulá-las poste-riormente.
Em Python, as representações de strings de números inteiros e números de ponto flutuante podem ser convertidas para os próprios números usando as funções int e float, respectivamente.
Ao ler dados de um arquivo, outra consideração importante é o formato dos itens de dados no arquivo.
Anteriormente, vimos um exemplo de segmento de código que produz números intei-ros separados por novas linhas em um arquivo de texto. Durante a entrada, esses dados podem ser lidos com um simples laço for. Esse laço acessa uma linha de texto em cada passagem. Para converter essa linha para o inteiro contido nela, o programador executa o método string strip para remover a nova linha e, em seguida, executa a função int para obter o valor inteiro.
O próximo segmento de código ilustra essa técnica.
Ele abre o arquivo de inteiros aleatórios gravado anteriormente, os lê e imprime a soma. """)

print()

f=open("Fundamentos_de_Python_estruturas_de_dados_pag_28.txt",'r')

soma = 0

for linha in f:
    linha = linha.strip()
    numero = int(linha)
    soma = soma + numero

print(f"A soma de todos os numeros é:{soma}")
f.close()