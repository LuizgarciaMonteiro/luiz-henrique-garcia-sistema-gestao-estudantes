from model.cursos import Curso
from model.disciplinas import Disciplina
from controller.controller_curso import Controller_Curso
from conexion.oracle_queries import OracleQueries

class Controller_Disciplina:
  def __init__(self):
    self.ctrl_curso = Controller_Curso()

  def inserir_disciplina(self) -> Disciplina:
    oracle = OracleQueries(can_write=True)
    oracle.connect()

    nome = input("Nome da disciplina (Nova): ")
    carga_horaria = input("Carga horária (horas): ")
    if not carga_horaria.isdigit():
      print("A carga horária deve ser um número inteiro.")
      return None

    # Escolha do curso ao qual a disciplina pertence
    self.ctrl_curso.listar_cursos(oracle)
    id_curso = input("ID do curso da disciplina: ")
    if not id_curso.isdigit() or not self.ctrl_curso.verifica_existencia_curso(oracle, id_curso):
      print(f"O curso {id_curso} não existe.")
      return None

    # Pede à sequence o próximo ID
    df_id = oracle.sqlToDataFrame("select disciplinas_id_disciplina_seq.nextval as id from dual")
    id_disciplina = int(df_id.id.values[0])

    # Insere e persiste a nova disciplina
    oracle.write(f"insert into disciplinas values ({id_disciplina}, '{nome}', {carga_horaria}, {id_curso})")

    # Recupera os dados e monta os objetos
    df_curso = oracle.sqlToDataFrame(f"select id_curso, nome, duracao_semestres from cursos where id_curso = {id_curso}")
    curso = Curso(df_curso.id_curso.values[0], df_curso.nome.values[0], df_curso.duracao_semestres.values[0])
    df_disciplina = oracle.sqlToDataFrame(f"select id_disciplina, nome, carga_horaria from disciplinas where id_disciplina = {id_disciplina}")
    nova_disciplina = Disciplina(df_disciplina.id_disciplina.values[0], df_disciplina.nome.values[0], df_disciplina.carga_horaria.values[0], curso)
    print(nova_disciplina.to_string())
    return nova_disciplina
