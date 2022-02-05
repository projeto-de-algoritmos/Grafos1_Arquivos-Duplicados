from sys import argv,exit
from utilitarios import Utilitarios

utilitarios = Utilitarios()

diretorio = utilitarios.uso()
utilitarios.mapearDiretorio(diretorio)

#utilitarios.mostrarArquivosMapeados()
utilitarios.mostrarDiretoriosMapeados()