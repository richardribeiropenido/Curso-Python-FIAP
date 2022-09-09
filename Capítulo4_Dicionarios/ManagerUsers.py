from Dicionarios1.Funcoes_Dicionarios import *
from Funcoes.Funcoes_Dicionarios import perguntar, inserir
usuarios = {}
opcao = perguntar()
while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L":
    if opcao=="I":
        inserir(usuarios)
        opcao = perguntar()



