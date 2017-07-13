from vertice import vertice

class grafo:

	def __init__(self, direcionado=False): 
		self._vertices = {}
		self.direcionado = direcionado

	def inserir_vertice(self, id):
		v = vertice(id)
		self._vertices[id] = v
		return v

	def inserir_aresta(self, de, para, peso=0):
		if de not in self._vertices:
			self.inserir_vertice(de)
		if para not in self._vertices:
			self.inserir_vertice(para)
		self._vertices[de].inserir_vertice_adjacente(self._vertices[para],peso)
		if not self.direcionado:
			self._vertices[para].inserir_vertice_adjacente(self._vertices[de],peso)

	def get_vertices(self):
		return ([v for k,v in self._vertices.iteritems()])

	def get_vertice(self, id):
		if id in self._vertices:
			return self._vertices[id]
		else:
			return None

	def get_arestas(self):
		arestas = set()
		for id, v in self._vertices.iteritems():
			for a in v._vertices_adjacentes:
				arestas.add((v,a))
		return arestas

	def __iter__(self):
		return iter(self._vertices.values())