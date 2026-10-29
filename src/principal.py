from utils import config
from utils.splash_screen import SplashScreen
from reports.relatorios import Relatorio
from controller.controller_curso import Controller_Curso
from controller.controller_disciplina import Controller_Disciplina
from controller.controller_aluno import Controller_Aluno
from controller.controller_nota import Controller_Nota

tela_inicial = SplashScreen()
relatorio = Relatorio()
ctrl_curso = Controller_Curso()
ctrl_disciplina = Controller_Disciplina()
ctrl_aluno = Controller_Aluno()
ctrl_nota = Controller_Nota()

def reports(opcao_relatorio:int=0):
  if opcao_relatorio == 1:
    relatorio.get_relatorio_media_por_turma()
  elif opcao_relatorio == 2:
    relatorio.get_relatorio_notas_alunos()

def inserir(opcao_inserir:int=0):
  if opcao_inserir == 1:
    ctrl_curso.inserir_curso()
  elif opcao_inserir == 2:
    ctrl_disciplina.inserir_disciplina()
  elif opcao_inserir == 3:
    ctrl_aluno.inserir_aluno()
  elif opcao_inserir == 4:
    ctrl_nota.inserir_nota()

def atualizar(opcao_atualizar:int=0):
  if opcao_atualizar == 1:
    ctrl_curso.atualizar_curso()
  elif opcao_atualizar == 2:
    ctrl_disciplina.atualizar_disciplina()
  elif opcao_atualizar == 3:
    ctrl_aluno.atualizar_aluno()
  elif opcao_atualizar == 4:
    ctrl_nota.atualizar_nota()

def excluir(opcao_excluir:int=0):
  if opcao_excluir == 1:
    ctrl_curso.excluir_curso()
  elif opcao_excluir == 2:
    ctrl_disciplina.excluir_disciplina()
  elif opcao_excluir == 3:
    ctrl_aluno.excluir_aluno()
  elif opcao_excluir == 4:
    ctrl_nota.excluir_nota()

def ler_opcao(mensagem:str, minimo:int, maximo:int) -> int:
  # Lê um número dentro do intervalo. Devolve -1 se for inválido
  try:
    opcao = int(input(mensagem))
  except ValueError:
    return -1
  if opcao < minimo or opcao > maximo:
    return -1
  return opcao

def deseja_continuar(pergunta:str) -> bool:
  return input(f"{pergunta} (S/N): ").strip().upper() == "S"

def executar_registros(opcao:int):
  # Associa cada opção do menu principal à sua ação e à pergunta de continuação
  acoes = {
    2: (inserir, "Deseja inserir mais algum registro?"),
    3: (atualizar, "Deseja atualizar mais algum registro?"),
    4: (excluir, "Deseja excluir mais algum registro?"),
  }
  acao, pergunta = acoes[opcao]

  while True:
    print(config.MENU_ENTIDADES)
    entidade = ler_opcao("Escolha uma opção [0-4]: ", 0, 4)
    config.clear_console(1)

    if entidade == 0:
      return
    if entidade == -1:
      print("Opção inválida.")
      continue

    acao(entidade)

    # Se a resposta for "Não", volta ao menu principal
    if not deseja_continuar(pergunta):
      return
    config.clear_console(1)

def run():
  print(tela_inicial.get_updated_screen())
  config.clear_console()

  while True:
    print(config.MENU_PRINCIPAL)
    opcao = ler_opcao("Escolha uma opção [1-5]: ", 1, 5)
    config.clear_console(1)

    if opcao == 1: # Relatórios
      while True:
        print(config.MENU_RELATORIOS)
        opcao_relatorio = ler_opcao("Escolha uma opção [0-2]: ", 0, 2)
        config.clear_console(1)

        if opcao_relatorio == 0:
          break
        if opcao_relatorio == -1:
          print("Opção inválida.")
          continue

        reports(opcao_relatorio)
        config.clear_console(1)

    elif opcao in (2, 3, 4): # Inserir, atualizar e remover registros
      executar_registros(opcao)
      config.clear_console(1)
      print(tela_inicial.get_updated_screen())
      config.clear_console()

    elif opcao == 5: # Sair
      print(tela_inicial.get_updated_screen())
      config.clear_console()
      print("Obrigado por utilizar o nosso sistema.")
      exit(0)

    else:
      print("Opção inválida.")

if __name__ == "__main__":
  run()
