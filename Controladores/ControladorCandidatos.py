from Repositorios.RepositorioCandidatos import RepositorioCandidatos
from Modelos.Candidatos import Candidatos

class ControladorCandidatos():
    def __init__(self):
        self.repositorioCandidatos = RepositorioCandidatos()
    def index(self):
        return self.repositorioCandidatos.findAll()
    def create(self,infoCandidatos):
        nuevoCandidatos=Candidatos(infoCandidatos)
        return self.repositorioCandidatos.save(nuevoCandidatos)
    def show(self,id):
        ElCandidato=Candidatos(self.repositorioCandidatos.findById(id))
        return ElCandidato.__dict__
    def update(self,id,infoCandidatos):
        CandidatosActual=Candidatos(self.repositorioCandidatos.findById(id))
        CandidatosActual.resolucion=infoCandidatos["resolucion"]
        CandidatosActual.cedula = infoCandidatos["cedula"]
        CandidatosActual.nombre = infoCandidatos["nombre"]
        CandidatosActual.apellido = infoCandidatos["apellido"]
        return self.repositorioCandidatos.save(CandidatosActual)
    def delete(self,id):
        return self.repositorioCandidatos.delete(id)