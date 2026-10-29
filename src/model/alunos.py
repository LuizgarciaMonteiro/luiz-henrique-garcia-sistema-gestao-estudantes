from model.cursos import Curso

class Aluno:
  def __init__ (self,
                matricula: str=None,
                nome: str=None,
                curso: Curso=None):
    self.set_matricula(matricula)
    self.set_nome(nome)
    self.set_curso(curso)

  def set_matricula(self, matricula:str):
    self.matricula = matricula

  def set_nome(self, nome:str):
    self.nome = nome

  def set_curso(self, curso:Curso):
    self.curso = curso

  def get_matricula(self) -> str:
    return self.matricula

  def get_nome(self) -> str:
    return self.nome

  def get_curso(self) -> Curso:
    return self.curso

  def to_string(self) -> str:
    return f"Matrícula: {self.get_matricula()} | Nome: {self.get_nome()} | Curso: {self.get_curso().get_nome()}"
