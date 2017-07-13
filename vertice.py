class vertice:

	def __init__(self, id): 
		self._id = id 
		self._vertices_adjacentes = {}
		self._distancia = 0
		self._visitado  = False
		self._anterior = None

	def get_id(self):
		return self._id

	def inserir_vertice_adjacente(self, para=None, peso=0):
		self._vertices_adjacentes[para] = peso

	def get_vertices_adjacentes(self):
		return self._vertices_adjacentes.keys() 

	def get_distancia(self):
		return self._distancia

	def set_distancia(self, distancia):
		self._distancia = distancia

	def set_visitado(self):
		self._visitado = True

	def get_visitado(self):
		return self._visitado

	def get_peso(self,para):
		return self._vertices_adjacentes[para]

	def set_anterior(self,anterior):
		self._anterior = anterior

	def get_anterior(self):
		return self._anterior

	def __str__(self):
		return str(self._id)