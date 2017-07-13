from grafo import grafo
from bellman_ford import bellman_ford
from utils import caminho_minino
import sys

class peso_negativo(Exception):
    pass

def test():

	print 'Testando um grafo com ciclo negativo'

	g = grafo(direcionado=True)
	
	g.inserir_vertice('a')
	g.inserir_vertice('b')
	g.inserir_vertice('c')
	g.inserir_vertice('d')
	g.inserir_vertice('e')
	g.inserir_vertice('f')

	g.inserir_aresta('b','a',-3)
	g.inserir_aresta('a','c',5)
	g.inserir_aresta('c','b',2)
	g.inserir_aresta('d','b',4)
	g.inserir_aresta('d','c',5)
	g.inserir_aresta('c','f',-3)
	g.inserir_aresta('e','c',4)
	g.inserir_aresta('e','f',5)
	g.inserir_aresta('f','d',-4)

	if bellman_ford(g,'a'):
		for v in g.get_vertices():
			caminho = [v.get_id()]	
			caminho_minino(v, caminho)
			print 'O menor caminho é: %s com custo %d.' %(caminho[::-1], v.get_distancia())	
	else:
		print 'Ciclo negativo encontrado'

if __name__ == "__main__":
	test()