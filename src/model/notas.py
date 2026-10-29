from model.alunos import Aluno
from model.disciplinas import Disciplina

class Nota:
  def __init__ (self,
                id_nota: int=None,
                aluno: Aluno=None,
                disciplina: Disciplina=None,
                semestre: str=None,
                atividade: str=None,
                nota: float=None):
    self.set_id_nota(id_nota)
    self.set_aluno(aluno)
    self.set_disciplina(disciplina)
    self.set_semestre(semestre)
    self.set_atividade(atividade)
    self.set_nota(nota)

  def set_id_nota(self, id_nota:int):
    self.id_nota = id_nota

  def set_aluno(self, aluno:Aluno):
    self.aluno = aluno

  def set_disciplina(self, disciplina:Disciplina):
    self.disciplina = disciplina

  def set_semestre(self, semestre:str):
    self.semestre = semestre

  def set_atividade(self, atividade:str):
    self.atividade = atividade

  def set_nota(self, nota:float):
    self.nota = nota

  def get_id_nota(self) -> int:
    return self.id_nota

  def get_aluno(self) -> Aluno:
    return self.aluno

  def get_disciplina(self) -> Disciplina:
    return self.disciplina

  def get_semestre(self) -> str:
    return self.semestre

  def get_atividade(self) -> str:
    return self.atividade

  def get_nota(self) -> float:
    return self.nota

  def to_string(self) -> str:
    return f"ID: {self.get_id_nota()} | Aluno: {self.get_aluno().get_nome()} | Disciplina: {self.get_disciplina().get_nome()} | Semestre: {self.get_semestre()} | Atividade: {self.get_atividade()} | Nota: {self.get_nota()}"
