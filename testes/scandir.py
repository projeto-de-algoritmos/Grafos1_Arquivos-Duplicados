from sys import argv,exit
from grafos import GrafoDirecionado, Path
from utilitarios import Utilitarios

utilitarios = Utilitarios()
grafo = GrafoDirecionado()

path1 = Path("pastas")
path2 = Path("pastas")

diretorio = utilitarios.uso()
utilitarios.mapearDiretorio(diretorio, grafo)
print(grafo.grafo)
print(grafo.dictAuxiliar)

# Mostra os arquivos de cada pasta
for key in list(grafo.grafo.keys()):
    print(grafo.dictAuxiliar[key].files)


#utilitarios.mostrarArquivosMapeados()
#utilitarios.mostrarDiretoriosMapeados()