from model.cursos import Curso
from conexion.oracle_queries import OracleQueries

class Controller_Curso:
  def __init__(self):
    pass

  def inserir_curso(self) -> Curso:
    # Cria uma nova conexão com o banco que permite alteração
    oracle = OracleQueries(can_write=True)
    oracle.connect()

    # Solicita os dados ao usuário
    nome = input("Nome do curso (Novo): ")
    duracao = input("Duração em semestres: ")
    if not duracao.isdigit():
      print("A duração deve ser um número inteiro.")
      return None

    # Pede à sequence o próximo ID
    df_id = oracle.sqlToDataFrame("select cursos_id_curso_seq.nextval as id from dual")
    id_curso = int(df_id.id.values[0])

    # Insere e persiste o novo curso
    oracle.write(f"insert into cursos values ({id_curso}, '{nome}', {duracao})")
    # Recupera o curso criado e monta o objeto
    df_curso = oracle.sqlToDataFrame(f"select id_curso, nome, duracao_semestres from cursos where id_curso = {id_curso}")
    novo_curso = Curso(df_curso.id_curso.values[0], df_curso.nome.values[0], df_curso.duracao_semestres.values[0])
    print(novo_curso.to_string())
    return novo_curso

  def atualizar_curso(self) -> Curso:
    oracle = OracleQueries(can_write=True)
    oracle.connect()

    # Lista os cursos para o usuário escolher
    self.listar_cursos(oracle)
    id_curso = input("ID do curso que deseja alterar: ")
    if not id_curso.isdigit():
      print("O ID deve ser um número inteiro.")
      return None

    if self.verifica_existencia_curso(oracle, id_curso):
      novo_nome = input("Nome (Novo): ")
      nova_duracao = input("Duração em semestres (Nova): ")
      if not nova_duracao.isdigit():
        print("A duração deve ser um número inteiro.")
        return None

      oracle.write(f"update cursos set nome = '{novo_nome}', duracao_semestres = {nova_duracao} where id_curso = {id_curso}")
      df_curso = oracle.sqlToDataFrame(f"select id_curso, nome, duracao_semestres from cursos where id_curso = {id_curso}")
      curso_atualizado = Curso(df_curso.id_curso.values[0], df_curso.nome.values[0], df_curso.duracao_semestres.values[0])
      print(curso_atualizado.to_string())
      return curso_atualizado
    else:
      print(f"O curso {id_curso} não existe.")
      return None

  def excluir_curso(self):
    oracle = OracleQueries(can_write=True)
    oracle.connect()

    self.listar_cursos(oracle)
    id_curso = input("ID do curso que deseja excluir: ")
    if not id_curso.isdigit():
      print("O ID deve ser um número inteiro.")
      return

    if not self.verifica_existencia_curso(oracle, id_curso):
      print(f"O curso {id_curso} não existe.")
      return

    # Confirmação antes de remover
    confirmacao = input("Deseja realmente excluir este curso? (S/N): ")
    if confirmacao.strip().upper() != "S":
      print("Exclusão cancelada.")
      return

    # Verifica se o curso é usado como FK em outras tabelas
    df_disciplinas = oracle.sqlToDataFrame(f"select count(1) as total from disciplinas where id_curso = {id_curso}")
    df_alunos = oracle.sqlToDataFrame(f"select count(1) as total from alunos where id_curso = {id_curso}")
    total_disciplinas = int(df_disciplinas.total.values[0])
    total_alunos = int(df_alunos.total.values[0])
    if total_disciplinas > 0 or total_alunos > 0:
      print(f"Este curso não pode ser excluído: possui {total_disciplinas} disciplina(s) e {total_alunos} aluno(s) vinculados.")
      return

    df_curso = oracle.sqlToDataFrame(f"select id_curso, nome, duracao_semestres from cursos where id_curso = {id_curso}")
    oracle.write(f"delete from cursos where id_curso = {id_curso}")
    curso_excluido = Curso(df_curso.id_curso.values[0], df_curso.nome.values[0], df_curso.duracao_semestres.values[0])
    print("Curso removido com sucesso!")
    print(curso_excluido.to_string())

  def listar_cursos(self, oracle:OracleQueries):
    print(oracle.sqlToDataFrame("select id_curso, nome from cursos order by id_curso"))

  def verifica_existencia_curso(self, oracle:OracleQueries, id_curso:str) -> bool:
    df_curso = oracle.sqlToDataFrame(f"select id_curso from cursos where id_curso = {id_curso}")
    return not df_curso.empty
