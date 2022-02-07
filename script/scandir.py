from sys import argv,exit
from grafos import GrafoDirecionado, Path
from utilitarios import Utilitarios

utilitarios = Utilitarios()
grafo = GrafoDirecionado()

path1 = Path("pastas")
path2 = Path("pastas")

diretorio = utilitarios.uso()
utilitarios.mapearDiretorio(diretorio, grafo)
utilitarios.comparaArquivos(grafo)
if (grafo.arquivosIdenticos == 0):
    print("Nenhum arquivo idêntico a partir deste diretório!")
