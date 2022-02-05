class GrafoDirecionado:
	
	def __init__(self):
		self.grafo = {}
		self.color = {}
		self.dfs_visited = set()
		self.bfs_visitado = {}
		
	def inserirVertice(self,vertice):
		if vertice in self.grafo:
			pass
		else:
			self.grafo[vertice] = []
			self.bfs_visitado[vertice] = False
	
	def inserirAresta(self,v1,v2):
		if v1 not in self.grafo:
			print(v1,' não existe no grafo')
		elif v2 not in self.grafo:
			print(v2,' não existe no grafo')
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
	
	def bipartition(self,vertice):
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
		return True
	
	def isBipartite(self):
   
		for v in self.grafo.keys(): 
			self.color[v] = -1
		
		for v in self.grafo.keys():
			if(self.color[v] == -1):
				if(not self.setColor(v, 0)):
					return False
		
		return True
	
	def setColor(self, v, c):
		self.color[v] = c
		for w in self.grafo[v]:
			if self.color[w] == -1:
				if self.setColor( w, (1-c)) == False:
					return False
			else:
				if self.color[w] == c:
					return False
		return True
