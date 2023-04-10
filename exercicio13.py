"""
Desenvolver um programa de computador que efetue a entrada do nome
e respectivo gênero de duas pessoas que pretendem formar um par para participar
de uma quadrilha em uma festa junina. Os admi-nistradores da festa determinaram
que somente serão aceitos pares heterogêneos (formados por pes-soas de sexos diferentes).
Para atender a este requisito, o programa deve, após a entrada do sexo das duas pessoas,
verificar se elas formam par, e no caso deve apresentar uma mensagem informando esta possibilidade.
Caso contrário, o programa deve indicar a impossibilidade de formação de par
"""
nome_1 = input("entre com seu nome:")
sexo_1 = input("entre com M masculino ou F feminino: ")
nome_2 = input("entre com seu nome:")
sexo_2 = input("entre com M masculino ou F feminino: ")

if sexo_1 == "M" or sexo_2 == "M":
    print (f"{nome_1} pode fazer par com {nome_2}")
else:
    print(f"{nome_1} não pode fazer par com {nome_2}")