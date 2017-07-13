from grafo import grafo
from bellman_ford import bellman_ford
from utils import caminho_minino
import sys

class peso_negativo(Exception):
    pass

def test():

	print 'Testando grafo de exemplo do livro Algoritmos 3rd (Cormen), página 480.'

	g = grafo(direcionado=True)
	
	g.inserir_vertice('a')
	g.inserir_vertice('b')
	g.inserir_vertice('c')
	g.inserir_vertice('d')
	g.inserir_vertice('e')

	g.inserir_aresta('a','b',6)
	g.inserir_aresta('a','c',7)
	g.inserir_aresta('a','e',2)
	g.inserir_aresta('b','d',5)
	g.inserir_aresta('b','c',8)
	g.inserir_aresta('b','e',-4)
	g.inserir_aresta('c','d',-3)
	g.inserir_aresta('c','e',9)
	g.inserir_aresta('d','b',-2)
	g.inserir_aresta('e','d',7)


	bellman_ford(g,'d')

	for v in g.get_vertices():
		caminho = [v.get_id()]	
		caminho_minino(v, caminho)
		print 'O menor caminho é: %s com custo %d.' %(caminho[::-1], v.get_distancia())	

if __name__ == "__main__":
	test()