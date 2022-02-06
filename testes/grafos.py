from distutils.log import error
from os import path
import codecs

class Path:

	def __init__(self, name) -> None:
		self.files = []
		self.visited = False
		self.name = name

class GrafoDirecionado:
	
	def __init__(self):
		self.grafo = {}
		self.bfs_visitado = {}
		self.dictAuxiliar = {}
		self.arquivosIdenticos = 0

	def __repr__(self) -> str:
		return self.grafo
		
	def inserirVertice(self,vertice):
		if vertice.name in self.grafo:
			pass
		else:
			self.grafo[vertice.name] = []
			self.dictAuxiliar[vertice.name] = vertice
	
	def inserirAresta(self,v1,v2):
		if v1 not in self.grafo:
			print(v1,' não existe no grafo - V1')
		elif v2 not in self.grafo:
			print(v2,' não existe no grafo - V2')
		else:
			self.grafo[v1].append(v2)
			
	def mostrarGrafo(self):
		for a in self.grafo:
			print(a,self.grafo[a])

	def verificaConteudoArquivos(self, arquivo1, pasta1, arquivo2, pasta2):
		caminho1 = path.join(pasta1.name, arquivo1)
		caminho2 = path.join(pasta2.name, arquivo2)

		file1 = codecs.open(caminho1, 'r', encoding='utf-8', errors='ignore')
		file2 = codecs.open(caminho2, 'r', encoding='utf-8', errors='ignore')

		for file1_line, file2_line in zip(file1, file2):
			if file1_line != file2_line:
				return
		self.arquivosIdenticos = self.arquivosIdenticos + 1
		print("Arquivos idênticos: {} e {}".format(caminho1, caminho2))

	def comparaArquivosOutroDiretorio(self, pasta: str, pastaComparar:Path):
		for file in pastaComparar.files:
			for arquivoComparador in self.dictAuxiliar[pasta].files:
				self.verificaConteudoArquivos(file, pastaComparar, arquivoComparador, self.dictAuxiliar[pasta])

	def comparaArquivosMesmoDiretorio(self, pasta: str):
		files = self.dictAuxiliar[pasta].files
		aux = files.copy()
		if len(aux) > 0:
			aux.pop(0)
		for file in files:
			for file2 in aux:
				if file != file2:
					self.verificaConteudoArquivos(file, self.dictAuxiliar[pasta], file2, self.dictAuxiliar[pasta])
			if len(aux) > 0:
				aux.pop(0)
	
	def bfs(self, pastaComparar: str, diretorioRaiz):
		fila = []
		
		fila.append(diretorioRaiz)

		while fila :
			pastaAtual = fila.pop(0)
			if not self.dictAuxiliar[pastaAtual].visited:
				self.comparaArquivosMesmoDiretorio(pastaAtual)
			for pasta in self.grafo[pastaAtual]:
				fila.append(pasta)
				if not self.dictAuxiliar[pasta].visited:
					if self.dictAuxiliar[pasta].name != self.dictAuxiliar[pastaComparar].name:
						self.comparaArquivosOutroDiretorio(pasta, self.dictAuxiliar[pastaComparar])
			self.dictAuxiliar[pastaComparar].visited = True

