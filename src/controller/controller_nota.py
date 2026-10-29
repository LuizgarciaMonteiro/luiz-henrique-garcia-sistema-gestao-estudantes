from model.notas import Nota
from controller.controller_aluno import Controller_Aluno
from controller.controller_disciplina import Controller_Disciplina
from conexion.oracle_queries import OracleQueries

class Controller_Nota:
  def __init__(self):
    self.ctrl_aluno = Controller_Aluno()
    self.ctrl_disciplina = Controller_Disciplina()

  def inserir_nota(self) -> Nota:
    oracle = OracleQueries(can_write=True)
    oracle.connect()

    # Escolha do aluno
    self.ctrl_aluno.listar_alunos(oracle)
    matricula = input("Matrícula do aluno: ").strip()
    if not self.ctrl_aluno.verifica_existencia_aluno(oracle, matricula):
      print(f"A matrícula {matricula} não existe.")
      return None

    # Escolha da disciplina
    self.ctrl_disciplina.listar_disciplinas(oracle)
    id_disciplina = input("ID da disciplina: ")
    if not id_disciplina.isdigit() or not self.ctrl_disciplina.verifica_existencia_disciplina(oracle, id_disciplina):
      print(f"A disciplina {id_disciplina} não existe.")
      return None

    # Semestre, atividade e valor da nota
    semestre = input("Semestre (ex.: 2026/2): ").strip()
    if len(semestre) != 6 or semestre[4] != "/":
      print("O semestre deve estar no formato AAAA/S, por exemplo 2026/2.")
      return None
    atividade = input("Atividade (ex.: Prova 1): ")
    valor = self.ler_nota("Nota (0 a 10): ")
    if valor is None:
      return None

    # Pede à sequence o próximo ID
    df_id = oracle.sqlToDataFrame("select notas_id_nota_seq.nextval as id from dual")
    id_nota = int(df_id.id.values[0])

    oracle.write(f"insert into notas values ({id_nota}, '{matricula}', {id_disciplina}, '{semestre}', '{atividade}', {valor})")
    nova_nota = self.buscar_nota(oracle, id_nota)
    print(nova_nota.to_string())
    return nova_nota

  def ler_nota(self, mensagem:str) -> float:
    try:
      valor = float(input(mensagem).replace(",", "."))
    except ValueError:
      print("A nota deve ser um número.")
      return None
    if valor < 0 or valor > 10:
      print("A nota deve estar entre 0 e 10.")
      return None
    return valor

  def buscar_nota(self, oracle:OracleQueries, id_nota:int) -> Nota:
    df = oracle.sqlToDataFrame(f"select id_nota, matricula, id_disciplina, semestre, atividade, nota from notas where id_nota = {id_nota}")
    aluno = self.ctrl_aluno.buscar_aluno(oracle, df.matricula.values[0])
    disciplina = self.ctrl_disciplina.buscar_disciplina(oracle, df.id_disciplina.values[0])
    return Nota(df.id_nota.values[0], aluno, disciplina, df.semestre.values[0], df.atividade.values[0], float(df.nota.values[0]))



  def atualizar_nota(self) -> Nota:
    oracle = OracleQueries(can_write=True)
    oracle.connect()

    self.listar_notas(oracle)
    id_nota = input("ID da nota que deseja alterar: ")
    if not id_nota.isdigit() or not self.verifica_existencia_nota(oracle, id_nota):
      print(f"A nota {id_nota} não existe.")
      return None

    nova_atividade = input("Atividade (Nova): ")
    novo_semestre = input("Semestre (Novo, ex.: 2026/2): ").strip()
    if len(novo_semestre) != 6 or novo_semestre[4] != "/":
      print("O semestre deve estar no formato AAAA/S, por exemplo 2026/2.")
      return None
    novo_valor = self.ler_nota("Nota (Nova, 0 a 10): ")
    if novo_valor is None:
      return None

    oracle.write(f"update notas set atividade = '{nova_atividade}', semestre = '{novo_semestre}', nota = {novo_valor} where id_nota = {id_nota}")
    nota_atualizada = self.buscar_nota(oracle, id_nota)
    print(nota_atualizada.to_string())
    return nota_atualizada

  def listar_notas(self, oracle:OracleQueries):
    print(oracle.sqlToDataFrame("select n.id_nota, a.nome as aluno, d.nome as disciplina, n.atividade, n.nota from notas n inner join alunos a on a.matricula = n.matricula inner join disciplinas d on d.id_disciplina = n.id_disciplina order by n.id_nota"))

  def verifica_existencia_nota(self, oracle:OracleQueries, id_nota:str) -> bool:
    df_nota = oracle.sqlToDataFrame(f"select id_nota from notas where id_nota = {id_nota}")
    return not df_nota.empty

  def excluir_nota(self):
    oracle = OracleQueries(can_write=True)
    oracle.connect()

    self.listar_notas(oracle)
    id_nota = input("ID da nota que deseja excluir: ")
    if not id_nota.isdigit() or not self.verifica_existencia_nota(oracle, id_nota):
      print(f"A nota {id_nota} não existe.")
      return

    # Confirmação antes de remover
    confirmacao = input("Deseja realmente excluir esta nota? (S/N): ")
    if confirmacao.strip().upper() != "S":
      print("Exclusão cancelada.")
      return

    # A nota não é usada como FK em nenhuma tabela, então pode ser removida
    nota_excluida = self.buscar_nota(oracle, id_nota)
    oracle.write(f"delete from notas where id_nota = {id_nota}")
    print("Nota removida com sucesso!")
    print(nota_excluida.to_string())
