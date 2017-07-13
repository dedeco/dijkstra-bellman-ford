import sys 

def initialize_single_source(g,s):	
	for v in g.get_vertices():
		v.set_distancia(sys.maxint)
	
	g.get_vertice(s).set_distancia(0)

def extract_min(Q):
	min = Q[0]
	for v in Q:
		if v.get_distancia() <min.get_distancia():
			min = v
	Q.remove(min) 
	return min

def relax(u,v):
	if v.get_distancia() > u.get_distancia() + u.get_peso(v):
		v.set_distancia(u.get_distancia() + u.get_peso(v))
		v.set_anterior(u)

def caminho_minino(v, caminho):    
    if v._anterior:
        caminho.append(v.get_anterior().get_id())
        caminho_minino(v.get_anterior(), caminho)
    return