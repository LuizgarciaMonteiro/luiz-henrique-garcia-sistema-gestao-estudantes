from conexion.oracle_queries import OracleQueries

class Relatorio:
  def __init__(self):
    # Abre o arquivo com a consulta e associa a um atributo da classe
    with open("sql/relatorio_media_por_turma.sql") as f:
      self.query_relatorio_media_por_turma = f.read()

    # Abre o arquivo com a consulta e associa a um atributo da classe
    with open("sql/relatorio_notas_alunos.sql") as f:
      self.query_relatorio_notas_alunos = f.read()

  def get_relatorio_media_por_turma(self):
    # Cria uma nova conexão com o banco
    oracle = OracleQueries()
    oracle.connect()
    # Recupera os dados transformando em um DataFrame
    print(oracle.sqlToDataFrame(self.query_relatorio_media_por_turma))
    input("Pressione Enter para sair do Relatório de Média por Turma")

  def get_relatorio_notas_alunos(self):
    oracle = OracleQueries()
    oracle.connect()
    print(oracle.sqlToDataFrame(self.query_relatorio_notas_alunos))
    input("Pressione Enter para sair do Relatório de Notas dos Alunos")
