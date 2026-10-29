class Curso:
  def __init__ (self,
                id_curso: int=None,
                nome: str=None,
                duracao_semestres: int=None):
    self.set_id_curso(id_curso)
    self.set_nome(nome)
    self.set_duracao_semestres(duracao_semestres)

  def set_id_curso(self, id_curso:int):
    self.id_curso = id_curso


  def set_nome(self, nome:str):
    self.nome = nome

  def set_duracao_semestres(self, duracao_semestres:int):
    self.duracao_semestres = duracao_semestres

  def get_id_curso(self) -> int:
    return self.id_curso

  def get_nome(self) -> str:
    return self.nome

  def get_duracao_semestres(self) -> int:
    return self.duracao_semestres

  def to_string(self) -> str:
    return f"ID: {self.get_id_curso()} | Nome: {self.get_nome()} | Duração: {self.get_duracao_semestres()} semestres"


