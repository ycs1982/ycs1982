print("""Você pode carregar objetos armazenados em um programa a partir de um arquivo usando a
função pickle.load. Se o final do arquivo foi alcançado, essa função irá gerar uma exceção.
Isso complica o processo de entrada, porque você não tem uma maneira aparente de detectar o final do
arquivo antes que a exceção seja levantada. Mas a instrução try-except do Python vem em seu socorro.
Essa instrução permite que uma exceção seja detectada e o programa se recupere.
Agora você pode construir um laço de arquivo de entrada que continua a carregar objetos até o final
do arquivo ser encontrado. Quando isso acontece, um EOFError é apresentado.
A cláusula except então fecha o arquivo e sai do laço. Eis o código para carregar objetos do arquivo items.
dat em uma nova lista chamada lista:
""")


import pickle

lista = list()


arquivo_objeto = open("item.dat", 'rb')

while True:
    try:
        item = pickle.load(arquivo_objeto)
        lista.append(item)
    except EOFError:
        arquivo_objeto.close()
        break
print(lista)

arquivo_objeto.close()