from Repositorios.RepositorioPartidoPolitico import RepositorioPartidoPolitico
from Modelos.PartidoPolitico import PartidoPolitico

class ControladorPartidoPolitico():
    def __init__(self):
        self.repositorioPartidoPolitico = RepositorioPartidoPolitico()
    def index(self):
        return self.repositorioPartidoPolitico.findAll()
    def create(self,infoPartidoPolitico):
        nuevoPartidoPolitico=PartidoPolitico(infoPartidoPolitico)
        return self.repositorioPartidoPolitico.save(nuevoPartidoPolitico)
    def show(self,id):
        ElPartidoPolitico=PartidoPolitico(self.repositorioPartidoPolitico.findById(id))
        return ElPartidoPolitico.__dict__
    def update(self,id,infoPartidoPolitico):
        PartidoPoliticoActual=PartidoPolitico(self.repositorioPartidoPolitico.findById(id))
        PartidoPoliticoActual.nombreDelPartido=infoPartidoPolitico["nombreDelPartido"]
        PartidoPoliticoActual.lemaDelPartido = infoPartidoPolitico["lemaDelPartido"]
        return self.repositorioPartidoPolitico.save(PartidoPoliticoActual)
    def delete(self,id):
        return self.repositorioPartidoPolitico.delete(id)