from model.cursos import Curso

class Disciplina:
  def __init__ (self,
                id_disciplina: int=None,
                nome: str=None,
                carga_horaria: int=None,
                curso: Curso=None):
    self.set_id_disciplina(id_disciplina)
    self.set_nome(nome)
    self.set_carga_horaria(carga_horaria)
    self.set_curso(curso)

  def set_id_disciplina(self, id_disciplina:int):
    self.id_disciplina = id_disciplina

  def set_nome(self, nome:str):
    self.nome = nome

  def set_carga_horaria(self, carga_horaria:int):
    self.carga_horaria = carga_horaria

  def set_curso(self, curso:Curso):
    self.curso = curso

  def get_id_disciplina(self) -> int:
    return self.id_disciplina

  def get_nome(self) -> str:
    return self.nome

  def get_carga_horaria(self) -> int:
    return self.carga_horaria

  def get_curso(self) -> Curso:
    return self.curso

  def to_string(self) -> str:
    return f"ID: {self.get_id_disciplina()} | Nome: {self.get_nome()} | Carga horária: {self.get_carga_horaria()}h | Curso: {self.get_curso().get_nome()}"
