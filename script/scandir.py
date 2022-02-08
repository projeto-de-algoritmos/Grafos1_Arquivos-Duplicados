from grafos import GrafoDirecionado
from utilitarios import Utilitarios

utilitarios = Utilitarios()
grafo = GrafoDirecionado()

diretorio = utilitarios.uso()
utilitarios.mapearDiretorio(diretorio, grafo)
utilitarios.comparaArquivos(grafo)
if (grafo.arquivosIdenticos == 0):
    print("Nenhum arquivo idêntico a partir deste diretório!")
