from utils import initialize_single_source, extract_min, relax

def dijkstra(g,s):

	initialize_single_source(g,s)	

	S = []
	Q = [v for v in g.get_vertices()]

	while len(Q):

		u = extract_min(Q)

		u.set_visitado()

		S.append(u)

		for v in u.get_vertices_adjacentes():

			if v.get_visitado():
				continue

			relax(u,v)