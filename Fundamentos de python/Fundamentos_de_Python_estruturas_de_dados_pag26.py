arquivo = open("Fundamentos_de_Python_estruturas_de_dados_pag26.txt", "r+")
arquivo.write("primeira linha\nsegunda linha\nterceira linha\n" + ",")
arquivo.write("teste\n")
arquivo.write("teste")
arquivo.close()

texto = open("Fundamentos_de_Python_estruturas_de_dados_pag26.txt", "r")

leitura = texto.read()
print(leitura)
