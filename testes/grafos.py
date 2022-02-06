class GrafoDirecionado:
	
	def __init__(self):
		self.grafo = {}
		self.bfs_visitado = {}
		self.dictAuxiliar = {}

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
	
	def dfs(self,vertice):
		if vertice not in self.dfs_visited:
			print(vertice)
			self.dfs_visited.add(vertice)
			for i in self.grafo[vertice]:
				self.dfs(i)
	
	def bfs(self,vertice):
		fila = []
		
		fila.append(vertice)
		self.bfs_visitado[vertice] = True

		while fila :
			vertice = fila.pop(0)
			print(vertice, end=' ')
			
			for i in self.grafo[vertice]:
				if self.bfs_visitado[i] == False:
					fila.append(i)
					self.bfs_visitado[i] = True
		print()

class Path:

	def __init__(self, name) -> None:
		self.files = []
		self.compared = False
		self.name = name

