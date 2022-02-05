from os import listdir,path,getcwd
from sys import argv,exit

class Utilitarios:

    def __init__(self):
        self.arquivosMapeados = {}
        self.diretoriosMapeados = []

    def uso(self):
        try:   
            return str(argv[1])  
        except IndexError:  
            print('''
                \tUso : {} [DIRETORIO]
                \t Se a pasta tiver espaço no nome , digite: {} "[DIRETORIO COM ESPAÇO]" 
            '''.format(argv[0]))
            exit()

    def mapearDiretorio(self,diretorioRaiz):
        try:
            diretorioRaizObj = listdir(diretorioRaiz)
        except:
            print('Erro na leitura do diretorio {}'.format(diretorioRaiz))
            pass

        for dado in diretorioRaizObj :
            #diretorioCorrente = getcwd()
            #print(dado if path.isfile(path.join(diretorioRaiz,dado)) else '{}/'.format(dado))
            
            caminhoCompleto = path.join(diretorioRaiz,dado)
            if path.isdir(caminhoCompleto):
                self.diretoriosMapeados.append(caminhoCompleto)
            else:
                self.arquivosMapeados[dado] = caminhoCompleto
    
    def mostrarArquivosMapeados(self):
        for diretorio in self.arquivosMapeados :
            print(self.arquivosMapeados[diretorio],diretorio)
    
    def mostrarDiretoriosMapeados(self):
        for a in range(len(self.diretoriosMapeados)):
            print(self.diretoriosMapeados[a])

'''for a in range(len(self.diretoriosMapeados)):
            self.mapearDiretorio('{}'.format(self.diretoriosMapeados[a]))
        return'''