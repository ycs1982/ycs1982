print("""você pode converter qualquer objeto em texto para armazenamento, mas o mapeamento
de objetos complexos para texto e vice-versa pode ser entediante e causar dores de cabeça com manutenção.
Felizmente, o Python inclui um módulo que permite ao programador salvar e car-regar objetos usando
um processo chamado pickling. O termo vem do processo de conversão de pepinos em picles para preservação
em potes. Entretanto, no caso dos objetos computacio-nais, você pode obter os pepinos de volta.
Qualquer objeto pode ser conservado antes de ser salvo em um arquivo e, em seguida, “retirado” à medida
que você o carrega de um arquivo para um programa. O Python cuida de todos os detalhes de conversão
automaticamente. Você começa importando o módulo pickling. Os arquivos são abertos para entrada e
saída usando os flags "rb" e "wb" (para fluxos de bytes) e fechados da maneira usual.
Para salvar um objeto, você usa a função pickle.dump. O primeiro argumento é o objeto a ir para o
“dump” ou ser salvo em um arquivo e o segundo argumento é o objeto de arquivo.
Por exemplo, você pode usar o módulo pickle para salvar os objetos em uma lista chamada lyst para um
arquivo denominado items.dat. Não é preciso saber quais tipos de objetos estão na lista ou quantos
objetos existem. Eis o código:""")

import pickle

lista = [60, "Uma string ojeto", 1977]

arquivo_objeto = open("item.dat", 'wb')

for item in lista:
    pickle.dump(item,arquivo_objeto)

arquivo_objeto.close()