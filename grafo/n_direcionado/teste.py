from ListaDeAdjacenciaGND import GrafoNaoDirecionado 

g = GrafoNaoDirecionado()
g.inserirVertice('a')
g.inserirVertice('b')
g.inserirVertice('c')
g.inserirVertice('d')
g.inserirVertice('e')
g.inserirVertice('f')
g.inserirVertice('g')

g.inserirAresta('a','b')
g.inserirAresta('b','e')
g.inserirAresta('a','c')
g.inserirAresta('a','d')
g.inserirAresta('b','d')
g.inserirAresta('c','d')
g.inserirAresta('e','d')
g.inserirAresta('f','g')

print(g.mostrarGrafo())
