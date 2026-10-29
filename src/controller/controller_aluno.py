from model.cursos import Curso
from model.alunos import Aluno
from controller.controller_curso import Controller_Curso
from conexion.oracle_queries import OracleQueries

class Controller_Aluno:
  def __init__(self):
    self.ctrl_curso = Controller_Curso()

  def inserir_aluno(self) -> Aluno:
    oracle = OracleQueries(can_write=True)
    oracle.connect()

    # A matrícula é digitada pelo usuário, então precisa ser verificada
    matricula = input("Matrícula (Nova): ").strip()
    if matricula == "":
      print("A matrícula não pode ser vazia.")
      return None
    if self.verifica_existencia_aluno(oracle, matricula):
      print(f"A matrícula {matricula} já está cadastrada.")
      return None

    nome = input("Nome (Novo): ")

    # Escolha do curso do aluno
    self.ctrl_curso.listar_cursos(oracle)
    id_curso = input("ID do curso do aluno: ")
    if not id_curso.isdigit() or not self.ctrl_curso.verifica_existencia_curso(oracle, id_curso):
      print(f"O curso {id_curso} não existe.")
      return None

    oracle.write(f"insert into alunos values ('{matricula}', '{nome}', {id_curso})")
    novo_aluno = self.buscar_aluno(oracle, matricula)
    print(novo_aluno.to_string())
    return novo_aluno

  def verifica_existencia_aluno(self, oracle:OracleQueries, matricula:str) -> bool:
    df_aluno = oracle.sqlToDataFrame(f"select matricula from alunos where matricula = '{matricula}'")
    return not df_aluno.empty

  def buscar_aluno(self, oracle:OracleQueries, matricula:str) -> Aluno:
    df = oracle.sqlToDataFrame(f"select a.matricula, a.nome, c.id_curso, c.nome as nome_curso, c.duracao_semestres from alunos a inner join cursos c on c.id_curso = a.id_curso where a.matricula = '{matricula}'")
    curso = Curso(df.id_curso.values[0], df.nome_curso.values[0], df.duracao_semestres.values[0])
    return Aluno(df.matricula.values[0], df.nome.values[0], curso)
