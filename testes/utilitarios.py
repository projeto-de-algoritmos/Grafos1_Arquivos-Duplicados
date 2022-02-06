from os import listdir,path,getcwd
from sys import argv,exit
from unicodedata import name

from grafos import GrafoDirecionado, Path

class Utilitarios:

    def __init__(self):
        self.arquivosMapeados = {}
        self.diretoriosMapeados = []

    def uso(self):
        try:
            return str(argv[1])  
        except IndexError:
            print('''
            Para correta utilização do programa, passe algum diretório como argumento:
            python {} [DIRETORIO]

            Em ocasiões em que o nome do diretório tenha espaço utilize "":
            python {} "pasta com espaco"
            '''.format(argv[0], argv[0]))  
            exit()

    def mapearDiretorio(self,diretorioRaiz, grafo: GrafoDirecionado):
        try:
            diretorioRaizObj = listdir(diretorioRaiz)
        except:
            print('Erro na leitura do diretorio {}'.format(diretorioRaiz))
            exit()

        novaPasta = Path(name=diretorioRaiz)
        diretoriosMapeados = []
        caminhosMapeados = []
        for dado in diretorioRaizObj :
            caminhoCompleto = path.join(diretorioRaiz,dado)
            if path.isdir(caminhoCompleto):
                self.diretoriosMapeados.append(caminhoCompleto)
                caminhosMapeados.append(caminhoCompleto)
                diretoriosMapeados.append(dado)
            else:
                novaPasta.files.append(dado)
                self.arquivosMapeados[dado] = caminhoCompleto

        grafo.inserirVertice(novaPasta)
        for subpasta in caminhosMapeados:
            self.mapearDiretorio(subpasta, grafo)
            grafo.inserirAresta(novaPasta.name, subpasta)

        
    
    def mostrarArquivosMapeados(self):
        for diretorio in self.arquivosMapeados :
            print(self.arquivosMapeados[diretorio],diretorio)
    
    def mostrarDiretoriosMapeados(self):
        for a in range(len(self.diretoriosMapeados)):
            print(self.diretoriosMapeados[a])