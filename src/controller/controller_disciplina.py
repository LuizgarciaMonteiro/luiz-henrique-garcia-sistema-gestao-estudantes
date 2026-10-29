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


  def atualizar_disciplina(self) -> Disciplina:
    oracle = OracleQueries(can_write=True)
    oracle.connect()

    self.listar_disciplinas(oracle)
    id_disciplina = input("ID da disciplina que deseja alterar: ")
    if not id_disciplina.isdigit() or not self.verifica_existencia_disciplina(oracle, id_disciplina):
      print(f"A disciplina {id_disciplina} não existe.")
      return None

    novo_nome = input("Nome (Novo): ")
    nova_carga = input("Carga horária (Nova): ")
    if not nova_carga.isdigit():
      print("A carga horária deve ser um número inteiro.")
      return None

    self.ctrl_curso.listar_cursos(oracle)
    novo_id_curso = input("ID do curso (Novo): ")
    if not novo_id_curso.isdigit() or not self.ctrl_curso.verifica_existencia_curso(oracle, novo_id_curso):
      print(f"O curso {novo_id_curso} não existe.")
      return None

    oracle.write(f"update disciplinas set nome = '{novo_nome}', carga_horaria = {nova_carga}, id_curso = {novo_id_curso} where id_disciplina = {id_disciplina}")
    disciplina_atualizada = self.buscar_disciplina(oracle, id_disciplina)
    print(disciplina_atualizada.to_string())
    return disciplina_atualizada

  def listar_disciplinas(self, oracle:OracleQueries):
    print(oracle.sqlToDataFrame("select id_disciplina, nome from disciplinas order by id_disciplina"))

  def verifica_existencia_disciplina(self, oracle:OracleQueries, id_disciplina:str) -> bool:
    df_disciplina = oracle.sqlToDataFrame(f"select id_disciplina from disciplinas where id_disciplina = {id_disciplina}")
    return not df_disciplina.empty

  def buscar_disciplina(self, oracle:OracleQueries, id_disciplina:str) -> Disciplina:
    df = oracle.sqlToDataFrame(f"select d.id_disciplina, d.nome, d.carga_horaria, c.id_curso, c.nome as nome_curso, c.duracao_semestres from disciplinas d inner join cursos c on c.id_curso = d.id_curso where d.id_disciplina = {id_disciplina}")
    curso = Curso(df.id_curso.values[0], df.nome_curso.values[0], df.duracao_semestres.values[0])
    return Disciplina(df.id_disciplina.values[0], df.nome.values[0], df.carga_horaria.values[0], curso)
