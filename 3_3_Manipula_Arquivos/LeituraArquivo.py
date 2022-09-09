with open("teste.txt", "r") as arquivo:
    conteudo=arquivo.read()
print("O tipo de dado da variável", type(conteudo))
print("Conteúdo do arquivo:", conteudo)
