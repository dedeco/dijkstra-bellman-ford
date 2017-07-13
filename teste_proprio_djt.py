from grafo import grafo
from dijkstra import dijkstra
from utils import caminho_minino
import sys

class peso_negativo(Exception):
    pass

def test():

	print 'Testando um grafo qualquer gerado aliatoriamente por mim.'

	g = grafo(direcionado=True)
	
	g.inserir_vertice('a')
	g.inserir_vertice('b')
	g.inserir_vertice('c')
	g.inserir_vertice('d')
	g.inserir_vertice('e')
	g.inserir_vertice('f')
	g.inserir_vertice('g')
	g.inserir_vertice('h')
	g.inserir_vertice('i')
	g.inserir_vertice('j')

	g.inserir_aresta('a','b',10)
	g.inserir_aresta('a','c',5)
	g.inserir_aresta('a','g',1)
	g.inserir_aresta('a','f',6)
	g.inserir_aresta('b','c',2)
	g.inserir_aresta('b','d',1)
	g.inserir_aresta('c','b',3)
	g.inserir_aresta('c','d',9)
	g.inserir_aresta('c','e',2)
	g.inserir_aresta('c','g',4)
	g.inserir_aresta('d','i',4)
	g.inserir_aresta('e','i',8)
	g.inserir_aresta('e','h',4)
	g.inserir_aresta('e','d',6)
	g.inserir_aresta('f','g',6)
	g.inserir_aresta('g','h',8)
	g.inserir_aresta('h','i',9)
	g.inserir_aresta('j','a',3)
	g.inserir_aresta('j','i',5)

	dijkstra(g,'a')

	for v in g.get_vertices():
		caminho = [v.get_id()]	
		caminho_minino(v, caminho)
		print 'O menor caminho é: %s com custo %d.' %(caminho[::-1], v.get_distancia())	

if __name__ == "__main__":
	test()