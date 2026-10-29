from conexion.oracle_queries import OracleQueries
from utils import config

class SplashScreen:
  def __init__(self):
    # Nome(s) do(s) criador(es)
    self.created_by = "Luiz Henrique Garcia"
    self.professor = "Prof. M.Sc. Howard Roatti"
    self.disciplina = "Banco de Dados"
    self.semestre = "2026/2"

  def get_total(self, tabela:str):
    # Cria uma nova conexão com o banco
    oracle = OracleQueries()
    oracle.connect()
    # Monta a consulta de contagem e retorna o total de registros
    query = config.QUERY_COUNT.format(tabela=tabela)
    return oracle.sqlToDataFrame(query)[f"total_{tabela}"].values[0]

  def get_updated_screen(self):
    return f"""
    ########################################################
    #            SISTEMA DE GESTÃO DE ESTUDANTES
    #
    #  TOTAL DE REGISTROS:
    #      1 - CURSOS:        {str(self.get_total("cursos")).rjust(5)}
    #      2 - DISCIPLINAS:   {str(self.get_total("disciplinas")).rjust(5)}
    #      3 - ALUNOS:        {str(self.get_total("alunos")).rjust(5)}
    #      4 - NOTAS:         {str(self.get_total("notas")).rjust(5)}
    #
    #  CRIADO POR: {self.created_by}
    #
    #  PROFESSOR:  {self.professor}
    #
    #  DISCIPLINA: {self.disciplina}
    #              {self.semestre}
    ########################################################
    """
