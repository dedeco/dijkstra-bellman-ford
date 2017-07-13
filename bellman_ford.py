from utils import initialize_single_source, relax

def bellman_ford(g,s):

	initialize_single_source(g,s)

	for u in g.get_vertices():
		for u,v in g.get_arestas():
			if v.get_visitado():
				continue
			relax(u,v)

	for u,v in g.get_arestas():
		if v.get_distancia() > u.get_distancia() + u.get_peso(v):
			return False

	return True 